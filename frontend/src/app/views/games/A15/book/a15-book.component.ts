import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Book } from '@app/interfaces/a15';
import { A15Service } from '@app/services/a15.service';
import { SeoService } from '@app/services/seo.service';

@Component({
  templateUrl: 'a15-book.component.html',
  selector: 'a15-book',
})
export class A15BookComponent implements OnInit {

  loading = false;
  submitted = false;
  returnUrl: string;
  error: string = '';
  book: Book;
  colset: string;

  seoTitle: string;
  seoDesc: string;
  seoImage: string;
  seoURL: string;

  gameTitle: string;
  gameURL: string;
  imgURL: string;

  @Input()
  slugname: string = "";

  @Input()
  showNav: boolean = true;

  language = "";

constructor(
    private route: ActivatedRoute,
    private a15service: A15Service,
    protected seoService: SeoService) {
      if(this.route.snapshot.params.book != null) {
      this.slugname = this.route.snapshot.params.book;
    }
  }
  ngOnInit(): void {
    this.language = this.route.snapshot.params.language;
    if(this.showNav) {
      this.colset = "col-md-9 mx-auto "
    }
    this.a15service.getBook(this.slugname, this.language)
    .subscribe(book => {
        this.error =``;
        this.book = book;

        this.gameTitle = this.a15service.gameTitle[this.language];
        this.gameURL = this.a15service.gameURL;
        this.imgURL = this.a15service.imgURL;

        this.seoURL = `${this.gameURL}/recipe-books/${this.book.slugname}/${this.language}`;
        this.seoTitle = `${this.book.name} - ${this.gameTitle}`;
        this.seoDesc = `${this.book.desc}`
        this.seoImage = `${this.imgURL}items/${this.book.slugname}.webp`
        this.seoService.SEOSettings(this.seoURL, this.seoTitle, this.seoDesc, this.seoImage);
    },
    error => {
      this.error =`${error.status}`;
    });
  }
} 