import { Dialog } from '@angular/cdk/dialog';
import { Location } from '@angular/common';
import { Component } from '@angular/core';
import { UntypedFormBuilder } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { ActivatedRoute, Router } from '@angular/router';
import { DestroyService } from '@app/services/destroy.service';
import { SeoService } from '@app/services/seo.service';
import { BreadcrumbService } from '@app/services/breadcrumb.service';
import { Monster } from '@app/views/games/A22/_services/a22.interface';
import { A22Service } from '@app/views/games/A22/_services/a22.service';
import { CommonImports, MaterialFormImports } from '@app/views/games/_prototype/SharedModules/common-imports';
import { DialogUseComponent } from '@app/views/games/_prototype/dialog-use.component';
import { Observable } from 'rxjs';
import { map, startWith } from 'rxjs/operators';
import { A22MonsterComponent } from './a22-monster.component';

@Component({
  templateUrl: 'a22-monsterlist.component.html',
  providers: [DestroyService],
  standalone: true,
  imports: [...CommonImports, ...MaterialFormImports,
    A22MonsterComponent, MatButtonModule]
})

export class A22MonsterlistComponent extends DialogUseComponent {
  filteredMonsters: Observable<Monster[]>;

  constructor(
    protected cdkDialog: Dialog,
    protected readonly destroy$: DestroyService,
    protected router: Router,
    protected route: ActivatedRoute,
    protected location: Location,
    protected seoService: SeoService,
    protected breadcrumbService: BreadcrumbService,
    private formBuilder: UntypedFormBuilder,
    private a22service: A22Service,
  ) {
    super(destroy$, router, route, location, seoService, breadcrumbService, cdkDialog);
    this.component = A22MonsterComponent;
    this.pageForm = this.formBuilder.nonNullable.group({
      filtertext: '',
      type: '1'
    })
  }

  changeData() {
    this.gameService(this.a22service, 'monsters');
    this.genericSettings(`Monsters`, `The list of monsters in ${this.gameTitle}.`);
    this.pageForm.reset();
    return this.a22service.getMonsterList(this.language);
  }

  afterAssignment(): void {
    this.filteredMonsters = this.pageForm.valueChanges.pipe(
      startWith(null as Observable<Monster[]>),
      map((search: any) => search ? this.filterT(search.filtertext, search.type) : this.data.slice())
    );
  }

  private filterT(value: string, type: string): Monster[] {
    let list: Monster[];

    switch (type) {
      case "1":
        list = this.data;
        break;
      case "Small":
      case "Medium":
      case "Large":
        list = this.data.filter(mon => mon.size == type);
        break;
      default:
        list = this.data.filter(mon => mon.montype == type);
        break;
    }
    if (!value) {
      return list;
    }
    const filterValue = value.toLowerCase();
    return list.filter(mon => {
      return mon.name.toLowerCase().includes(filterValue);
    });
  }
}