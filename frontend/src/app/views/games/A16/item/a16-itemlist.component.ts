import { Location } from '@angular/common';
import { Component, OnInit, TemplateRef } from '@angular/core';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';
import { ActivatedRoute, NavigationEnd, Router } from '@angular/router';
import { Category, ItemList } from '@app/interfaces/a16';
import { A16Service } from '@app/services/a16.service';
import { SeoService } from '@app/services/seo.service';
import { BsModalRef, BsModalService, ModalOptions } from 'ngx-bootstrap/modal';
import { Observable } from 'rxjs';
import { map, startWith } from 'rxjs/operators';

@Component({
    templateUrl: 'a16-itemlist.component.html',
  })

  export class A16ItemlistComponent implements OnInit {
    modalRef: BsModalRef;
    pageForm: FormGroup;
    itemControl: FormControl;
    ingControl: FormControl;
    error: boolean = false;
    errorCode: string;
    item: string = "items";
    items: ItemList[];
    filteredItems: Observable<ItemList[]>;
    language = "";
    config: ModalOptions = { class: "col-md-5 mx-auto" };
    categories: Category[];
    selectedCat = "Any";
    selectedElem = "Any";
    selectedElemV = 0;
  
    seoTitle: string;
    seoDesc: string;
    seoImage: string;
    seoURL: string;

    gameTitle: string;
    gameURL: string;
    imgURL: string;
  
    constructor(
      private modalService: BsModalService,
      private router: Router,
      private formBuilder: FormBuilder,
      private route: ActivatedRoute,
      private location: Location,
      private a16service: A16Service,
      private seoService: SeoService
    ) { 
      this.itemControl = new FormControl();
      this.ingControl = new FormControl();

      this.pageForm = this.formBuilder.group({
        filtertext: this.itemControl,
        filtering: this.ingControl,
        type: ['Any'],
        elementval: [0],
        element: ["Any"]
      })
    }
  
    ngOnInit(): void {
  
      this.language = this.route.snapshot.params.language;
  
      this.getItems();
      this.getCategories();
      
      this.gameTitle = this.a16service.gameTitle[this.language];
      this.gameURL = this.a16service.gameURL;
      this.imgURL = this.a16service.imgURL;

      this.seoURL = `${this.gameURL}/items/${this.language}`;
      this.seoTitle = `Items - ${this.gameTitle}`;
      this.seoDesc = `The list of items in ${this.gameTitle}.`
      this.seoService.SEOSettings(this.seoURL, this.seoTitle, this.seoDesc, this.seoImage);

      this.router.events.subscribe(event => {
        if (event instanceof NavigationEnd) {
          this.modalService.setDismissReason('link');
          this.modalService.hide();
        }
      });
    }
  
    getItems() {
      this.a16service.getItemList(this.language)
      .subscribe(items => {
        this.items = items;
        this.filteredItems = this.pageForm.valueChanges.pipe(
          startWith(null as Observable<ItemList[]>),
          map((search: any) => search ? this.filterT(search.filtertext, search.type, search.elementval, search.element, search.filtering) : this.items.slice())
        );
      },
      error => {
        this.error = true;
        this.errorCode = `${error.status}`;
        
      });
    }

    getCategories() {
      this.a16service.getCategories(this.language)
      .subscribe({next: categories  => {
          this.categories = categories;
      },
      error: error => {
          this.error = true;
          this.errorCode = `${error.status}`;
      }});
  }
  
    openModal(template: TemplateRef<any>, slug: string, event?) {
      if (event) {
        if(event.ctrlKey) {
          return;
        }
        else {
          event.preventDefault()
        }
      }
      this.item = slug;
      this.location.go(`${this.gameURL}/items/` + slug + "/" + this.language);
      this.modalRef = this.modalService.show(template);
      this.modalRef.onHide.subscribe((reason: string | any) => {
        if(reason != "link") {
          this.location.go(`${this.gameURL}/items/` + this.language);
          this.seoService.SEOSettings(this.seoURL, this.seoTitle, this.seoDesc, this.seoImage);
        }})
    }
  
    private filterT(value: string, type: string, elementV: number, element: string, ing: string): ItemList[] {
      let list: ItemList[] = this.items;

      if(type != 'Any') {
          list = list.filter(item => item.categories.some(c => c.name == type) );
      }

      if(elementV > 1) {
          list = list.filter(item => item.evalue >= elementV);
      }

      switch(element) {
          case "Fire":
              list = list.filter(item => item.fire)
              break;
          case "Water":
            list = list.filter(item => item.water)
            break;
          case "Wind":
              list = list.filter(item => item.wind)
              break;
          case "Earth":
              list = list.filter(item => item.earth)
              break;
      }

      if(ing) {
          const filterValue = ing.toLowerCase();
          list = list.filter(item => (item.ingredient_set) ? item.ingredient_set.some(i => i.ing.toLowerCase().includes(filterValue)) : false)
      }

      if(value) {
        const filterValue = value.toLowerCase();
        list = list.filter(item => { 
            return item.name.toLowerCase().includes(filterValue);
          });
      }

      return list;
    } 
  
    get f() { return this.pageForm.controls; }

    identify(index, item){
      return item.slugname;
   }
  }