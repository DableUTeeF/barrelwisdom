
import { Location, ViewportScroller } from '@angular/common';
import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DestroyService } from '@app/services/destroy.service';
import { SeoService } from '@app/services/seo.service';
import { BreadcrumbService } from '@app/services/breadcrumb.service';
import { BR1Service } from '@app/views/games/BR1/_services/br1.service';
import { CommonImports } from '@app/views/games/_prototype/SharedModules/common-imports';
import { FragmentedComponent } from '@app/views/games/_prototype/fragmented.component';

@Component({
  templateUrl: 'br1-skilllist.component.html',
  providers: [DestroyService],
  standalone: true,
  imports: [...CommonImports]
})
export class BR1SkilllistComponent extends FragmentedComponent {
  constructor(
    protected route: ActivatedRoute,
    protected readonly destroy$: DestroyService,
    protected loc: Location,
    private br1service: BR1Service,
    protected seoService: SeoService,
    protected breadcrumbService: BreadcrumbService,
    protected viewportScroller: ViewportScroller) {
    super(destroy$, route, seoService, breadcrumbService, viewportScroller, loc);
  }
  changeData() {
    this.gameService(this.br1service, 'skills');
    this.genericSettings(`Skills`, `The full skill list in ${this.gameTitle}.`);
    return this.br1service.getSkillList(this.language);
  }
} 