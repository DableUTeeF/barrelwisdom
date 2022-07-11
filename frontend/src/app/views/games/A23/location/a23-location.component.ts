import { Location, ViewportScroller } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { UntypedFormBuilder, UntypedFormControl, UntypedFormGroup } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Area, GatherNode, Region } from '@app/views/games/A23/_services/a23.interface';
import { A23Service } from '@app/views/games/A23/_services/a23.service';
import { DestroyService } from '@app/services/destroy.service';
import { SeoService } from '@app/services/seo.service';
import { SingleComponent } from '@app/views/games/_prototype/single.component';
import { first, takeUntil } from 'rxjs/operators';

@Component({
  templateUrl: 'a23-location.component.html',
  providers: [DestroyService]
})

export class A23LocationComponent extends SingleComponent implements OnInit {
  pageForm: UntypedFormGroup;
  locationControl: UntypedFormControl;
  region: Region;
  filteredRegion: Area[];
  filteredNodes: GatherNode[];
  language: string;
  search: string = "";
  query: string = "";

  constructor(
    protected route: ActivatedRoute,
    protected seoService: SeoService,
    private a23service: A23Service,
    private readonly destroy$: DestroyService,
    private loc: Location,
    private router: Router,
    private viewportScroller: ViewportScroller,
    private formBuilder: UntypedFormBuilder,
  ) {
    super(route, seoService);
    this.gameService(this.a23service, 'locations');
    this.locationControl = new UntypedFormControl();
    this.pageForm = this.formBuilder.group({
      filtertext: this.locationControl,
    })
  }

  ngOnInit(): void {
    this.region = this.route.snapshot.data.loc;
    this.filteredRegion = this.region.areas;
    this.query = this.route.snapshot.queryParamMap.get('item');
    if (this.region.areas.length == 0 || !this.region) {
      this.error = `404`;
    }
    else {
      this.pageForm.get("filtertext").valueChanges
        .pipe(takeUntil(this.destroy$))
        .subscribe(filter => {
          this.filteredNodes = this.filterT(filter)
          this.search = filter;
        }
        );
      if (this.query) { this.pageForm.controls['filtertext'].patchValue(this.query); }
      this.genericSEO(this.region.name, `All items in ${this.region.name}`);
    }
  }

  ngAfterViewInit(): void {
    this.route.fragment.pipe(
      first(), takeUntil(this.destroy$)
    ).subscribe(fragment => this.viewportScroller.scrollToAnchor(fragment));
  }
  scroll(id: string) {
    this.loc.replaceState(`${this.gameURL}/${this.section}/${this.region.slug}/${this.language}#${id}`);
    this.viewportScroller.scrollToAnchor(id);
  }

  scrollTo(fragment): void {
    this.router.navigate([], { fragment: fragment }).then(() => {
      const element = document.getElementById(fragment);
      if (element != undefined) element.scrollIntoView();
    });
  }

  private filterT(value: string): GatherNode[] {
    let nodeList: GatherNode[] = [];

    if (!value) {
      return nodeList;
    }
    const filterValue = value.toLowerCase();
    for (let area of this.region.areas) {
      for (let climate of area.climate) {
        for (let node of climate.nodes) {
          if (node.items.some(item => item.name.toLowerCase().includes(filterValue))) {
            nodeList.push(node)
          }
        }
      }
    }
    return nodeList;
  }

  get f() { return this.pageForm.controls; }

  validNode(node: GatherNode): boolean {
    if (this.search.length === 0) return true;
    if (this.filteredNodes.indexOf(node) > -1) return true;
    return false;
  }
}