import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { DestroyService } from '@app/services/destroy.service';
import { SeoService } from '@app/services/seo.service';
import { BreadcrumbService } from '@app/services/breadcrumb.service';
import { Popover } from '@app/views/_components/popover/popover.component';
import { BRSLService } from '@app/views/games/BRSL/_services/brsl.service';
import { CommonImports } from '@app/views/games/_prototype/SharedModules/common-imports';
import { SingleComponent } from '@app/views/games/_prototype/single.component';

@Component({
  templateUrl: 'brsl-facility.component.html',
  selector: 'brsl-facility',
  providers: [DestroyService],
  standalone: true,
  imports: [...CommonImports, Popover]
})
export class BRSLFacilityComponent extends SingleComponent {
  expand = false;

  constructor(
    protected route: ActivatedRoute,
    protected readonly destroy$: DestroyService,
    protected seoService: SeoService,
    protected breadcrumbService: BreadcrumbService,
    protected brslservice: BRSLService) {
    super(destroy$, route, breadcrumbService, seoService);
  }
  changeData() {
    this.gameService(this.brslservice, 'facilities');
    return this.brslservice.getFacility(this.slug, this.language)
  }
  afterAssignment(): void {
    this.seoImage = `${this.imgURL}${this.section}/${this.data.slug}.webp`;
    this.genericSettings(this.data.name, this.data.desc,
      'Facilities',
      false,
      this.inputSlug ? false : true);
  }
} 