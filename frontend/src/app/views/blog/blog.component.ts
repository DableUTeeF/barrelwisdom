import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Blog } from '@app/interfaces/blog';
import { User } from '@app/interfaces/user';
import { BlogService } from '@app/services/blog.service';
import { ErrorCodeService } from "@app/services/errorcode.service";
import { SafeHtml } from '@angular/platform-browser';
import { AuthenticationService } from '@app/services/authentication.service';
import { MarkdownService } from 'ngx-markdown';
import { SeoService } from '@app/services/seo.service';
import { Meta, Title } from '@angular/platform-browser';

@Component({
    templateUrl: 'blog.component.html',
  })


  export class BlogComponent implements OnInit {
      user: User;
      blog: Blog;
      error: boolean = false;
      errorCode: string;
      errorVars: any[];
      body: SafeHtml;
      allowedToEdit = false;
      gameName = "";
      breadcrumbs = [["Barrel Wisdom", "/"]];

      constructor(
        private route: ActivatedRoute,
        private blogService: BlogService,
        private errorService: ErrorCodeService,
        private authenticationService: AuthenticationService,
        private markdownService: MarkdownService,
        private seoService: SeoService,
        private metaService: Meta,
        private titleService: Title) {

      }

      ngOnInit(): void {
        this.authenticationService.user.subscribe(x => this.user = x);
        this.route.paramMap.subscribe(params => {
          this.getBlog(params.get('section'), params.get('title'));
        })
        
      }

      getBlog(section: string, title: string): void {
        this.blogService.getBlog(title, section)
          .subscribe(blog => { 
              this.error = false;
              this.blog = blog;
              this.gameName = (this.blog.section.fullname) ? `${this.blog.section.fullname} - ` : ""; // gotta make sure google sees the game name...
              this.body = this.markdownService.compile(this.blog.body);
              if(this.user) {
                if(this.blog.authorlock && this.user.id == this.blog.author[0].id) {
                  this.allowedToEdit = true;
                }
                else if(this.user.group == 'admin') {
                  this.allowedToEdit = true;
                }
                else if(!this.blog.authorlock) {
                  if(this.user.group == 'trusted' || this.blog.section.name != 'blog') {
                    this.allowedToEdit = true;
                  }
                }
              }
              if(this.breadcrumbs.length > 1) {
                this.breadcrumbs.pop();
              }
              if(section != "blog") {
                this.titleService.setTitle(`${this.blog.title} - ${this.blog.section.fullname} - Barrel Wisdom`);
                this.breadcrumbs.push([this.blog.section.fullname, '/' + this.blog.section.name])
              }
              else {
                this.titleService.setTitle(`${this.blog.title} - Barrel Wisdom`);
              }
              this.seoService.createCanonicalURL(`${this.blog.section.name}/${this.blog.slugtitle}`);
              this.metaService.updateTag({ name: `robots`, content: `index, archive` },`name="robots"`);
              this.metaService.updateTag({ name: `description`, content: `${this.blog.description}` }, `name="description"`);
              this.metaService.updateTag({ property: `og:title`, content: `${this.blog.title}` }, `property="og:title"`);
              this.metaService.updateTag({ property: `og:description`, content: `${this.blog.description}` },`property="og:description"`);
              this.metaService.updateTag({ property: `og:type`, content: `webpage` }, `property="og:type"`);
              if(this.blog.image) {
                this.metaService.updateTag({ property: `og:image`, content: `${this.blog.image}` }, `property="og:image"`);
              }
              else {
                this.metaService.updateTag({ property: `og:image`, content: `/media/main/barrel.png` }, `property="og:image"`);
              }
            },
            error => { 
                this.error = true;
                this.errorCode = error.status.toString();
                this.errorVars = this.errorService.getCodes(this.errorCode);
              }
            );
      }
  }