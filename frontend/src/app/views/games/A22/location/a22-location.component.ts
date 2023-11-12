import { Location, ViewportScroller } from '@angular/common';
import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DestroyService } from '@app/services/destroy.service';
import { SeoService } from '@app/services/seo.service';
import { A22Service } from '@app/views/games/A22/_services/a22.service';
import { FragmentedComponent } from '@app/views/games/_prototype/fragmented.component';

@Component({
  templateUrl: 'a22-location.component.html',
  providers: [DestroyService]
})

export class A22LocationComponent extends FragmentedComponent {
  dig = true;

  constructor(
    protected route: ActivatedRoute,
    protected readonly destroy$: DestroyService,
    protected loc: Location,
    private a22service: A22Service,
    protected seoService: SeoService,
    protected viewportScroller: ViewportScroller) {
    super(destroy$, route, seoService, viewportScroller, loc);
  }

  changeData() {
    this.gameService(this.a22service, 'locations');
    return this.a22service.getLocation(this.slug, this.language);
  }

  afterAssignment(): void {
    this.genericSEO(this.data.name, `All items in ${this.data.name}`);
    for (let g of this.data.areas[0].gatherdata) {
      if (g.tool == 'Dig') {
        this.dig = true;
        break;
      }
      this.dig = false;
    }
  }
}