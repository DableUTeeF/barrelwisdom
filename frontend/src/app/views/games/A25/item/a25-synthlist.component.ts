import { Location } from '@angular/common';
import { Component, OnInit, TemplateRef } from '@angular/core';
import { UntypedFormBuilder, UntypedFormControl } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { DestroyService } from '@app/services/destroy.service';
import { SeoService } from '@app/services/seo.service';
import { NameLink, Item } from '@app/views/games/A25/_services/a25.interface';
import { A25Service } from '@app/views/games/A25/_services/a25.service';
import { ListComponent } from '@app/views/games/_prototype/list.component';
import { BsModalService } from 'ngx-bootstrap/modal';
import { Observable } from 'rxjs';
import { map, startWith, takeUntil } from 'rxjs/operators';

@Component({
  templateUrl: 'a25-synthlist.component.html',
  providers: [DestroyService]
})

export class A25SynthesisListComponent extends ListComponent implements OnInit {
  itemControl: UntypedFormControl;
  ingControl: UntypedFormControl;
  items: Item[];
  filteredItems: Observable<Item[]>;
  combat_type: NameLink[];
  equipment_type: NameLink[];

  constructor(
    protected modalService: BsModalService,
    protected readonly destroy$: DestroyService,
    protected router: Router,
    protected route: ActivatedRoute,
    protected location: Location,
    protected seoService: SeoService,
    private formBuilder: UntypedFormBuilder,
    private a25service: A25Service,
  ) {
    super(modalService, destroy$, router, route, location, seoService);
    this.gameService(this.a25service, 'items');
    this.itemControl = new UntypedFormControl();
    this.ingControl = new UntypedFormControl();
    this.pageForm = this.formBuilder.group({
      filtertext: this.itemControl,
      filtering: this.ingControl,
      kind: ['Any'],
      rarity: ['0']
    })
  }

  ngOnInit(): void {
    this.modalEvent();
    this.getItems();
    this.getTypes();
    this.genericSEO(`Items`, `The list of items in ${this.gameTitle}.`);
  }

  replaceVal(item: Item): string {
    if (item.equip) {
      if (item.equip[0].val_bad) {
        return item.desc.replace("{0}", `${item.equip[0].val_bad / 100} ~ ${item.equip[0].val_good / 100}`)
      }
      return item.desc.replace("{0}", ` ${item.equip[0].val_good / 100}`)
    }
    if (item.combat[0].val_bad) {
      return item.desc.replace("{0}", `${item.combat[0].val_bad / 100} ~ ${item.combat[0].val_good / 100}`)
    }
    return item.desc.replace("{0}", ` ${item.combat[0].val_good / 100}`)
  }

  getItems() {
    this.a25service.getSynthList(this.language)
      .pipe(takeUntil(this.destroy$))
      .subscribe({
        next: items => {
          this.items = items;
          this.filteredItems = this.pageForm.valueChanges.pipe(
            startWith(null as Observable<Item[]>),
            map((search: any) => search ? this.filterT(search.filtertext, search.kind, search.rarity, search.filtering) : this.items.slice())
          );
        },
        error: error => {
          this.error = `${error.status}`;
        }
      });
  }

  getTypes() {
    this.a25service.getFilter('equipment', this.language)
      .pipe(takeUntil(this.destroy$))
      .subscribe({
        next: o => {
          this.equipment_type = o;
        },
        error: error => {
          this.error = `${error.status}`;
        }
      });
    this.a25service.getFilter('combat_type', this.language)
      .pipe(takeUntil(this.destroy$))
      .subscribe({
        next: o => {
          this.combat_type = o;
        },
        error: error => {
          this.error = `${error.status}`;
        }
      });
  }

  private filterT(value: string, kind: string, rarity: number, filter: string): Item[] {
    let list: Item[] = this.items;

    if (kind != 'Any') {
      list = list.filter(item => item.equip ? item.equip[0].kind == kind : item.combat[0].kind == kind);
    }

    if (rarity > 0) {
      list = list.filter(item => item.rarity == rarity)
    }

    if (filter) {
      console.log(filter)
      filter = filter.toLowerCase()

      list = list.filter(item => item.ing.some(i => i.toLowerCase().includes(filter)))
    }

    if (value) {
      const filterValue = value.toLowerCase();
      list = list.filter(item => {
        return item.name.toLowerCase().includes(filterValue) || item.desc.toLowerCase().includes(filterValue);
      });
    }

    return list;
  }

  identify2(index, item) {
    return item.slug;
  }

  openModal(template: TemplateRef<any>, slug: string, event?) {
    if (event) {
      if (event.ctrlKey) {
        return;
      }
      else {
        event.preventDefault()
      }
    }
    this.selected = slug;
    this.location.go(`${this.gameURL}/${this.section}/synthesis/${slug}/${this.language}`);
    this.modalRef = this.modalService.show(template);
    this.modalRef.onHide
      .pipe(takeUntil(this.destroy$))
      .subscribe((reason: string | any) => {
        if (reason != "link") {
          this.location.go(`${this.gameURL}/${this.section}/synthesis/${this.language}`);
          this.seoService.SEOSettings(this.seoURL, this.seoTitle, this.seoDesc, this.seoImage);
        }
      })
  }
}