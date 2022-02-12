// Probably shoulda put all these in components for simpler repeated code, oh well

import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { SettingService } from '@app/services/setting.service';
import { ErrorCodeService } from '@app/services/errorcode.service';
import { first } from 'rxjs/operators';
import { User } from "@app/interfaces/user";
import { AuthenticationService } from "@app/services/authentication.service";
import { environment } from '@environments/environment';
import { SeoService } from '@app/services/seo.service';
import { Meta, Title } from '@angular/platform-browser';

@Component({
  templateUrl: 'settings.component.html',
})
export class SettingsComponent {
  profileForm: FormGroup;
  passwordForm: FormGroup;
  sectionForm: FormGroup;
  navigationForm: FormGroup;
  loading = false;
  submitted = false;
  submittedPass = false;
  submittedSection = false;
  submittedNavigation = false;
  returnUrl: string;
  errorMsg: string;
  errorPass: string;
  errorInvite: string;
  errorSection: string;
  errorNavigation: string;
  successProfile = false;
  successPassword = false;
  successSection = false;
  successNavigation = false;
  user: User;
  invite: string;
  sections: any[];

  constructor(
    private formBuilder: FormBuilder,
    private route: ActivatedRoute,
    private settingService: SettingService,
    private errorCodeService: ErrorCodeService,
    private authenticationService: AuthenticationService,
    private seoService: SeoService,
    private metaService: Meta,
    private titleService: Title
    ) {
      this.authenticationService.user.subscribe(x => this.user = x);
    }

    ngOnInit() {
      this.seoService.removeCanonicalURL();
      this.titleService.setTitle(`Settings - Barrel Wisdom`);
      this.metaService.updateTag({ name: `robots`, content: `noindex` },`name="robots"`);

      if(this.user.group == "admin") {
        this.settingService.getSections().subscribe(sections => {
          this.sections = sections;
        });
      }

      this.passwordForm = this.formBuilder.group({
        newPass: ['', [Validators.required, Validators.minLength(8)]],
        repeatPass: ['', Validators.required],
        currentPass: ['', [Validators.required]],
      });

      this.profileForm = this.formBuilder.group({
        bio: ['', [Validators.maxLength(500)]],
        website: ['', [Validators.pattern('(https?://)?([\\da-z.-]+)\\.([a-z.]{2,6})[/\\w .-]*/?'), Validators.maxLength(200)]],
        avatar: ['', [Validators.pattern(environment.imageRegex + '.+\\.(png|jpg)'), Validators.maxLength(200)]],
      });

      this.sectionForm = this.formBuilder.group({
        name: ['', [Validators.required, Validators.maxLength(30)]],
        fullname: ['', [Validators.required, Validators.maxLength(30)]]
      });

      this.navigationForm = this.formBuilder.group({
        section: [''],
        data: ['', [Validators.required]]
      });

      this.loadProfile(this.user.id);

      this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
  }


  get profilef() { return this.profileForm.controls; }
  get passwordf() { return this.passwordForm.controls; }
  get sectionf() { return this.sectionForm.controls; }
  get navigationf() { return this.navigationForm.controls; }

  loadProfile(id: number) {
    if(id != null) {
      this.settingService.getProfile(id)
      .subscribe({next: profile => {
        this.profileForm.get('bio').setValue(profile.bio);
        this.profileForm.get('website').setValue(profile.website);
        this.profileForm.get('avatar').setValue(profile.avatar);
        this.loading = false;
      },
        error: error => {
          this.loading = false;
          this.errorCodeService.errorMessage(error);
      }});
    }
  }

  submitProfile() {
    this.submitted = true;
    this.successProfile = false;

    if (this.profileForm.invalid) {
      return;
    }

    this.loading = true;
    this.settingService.updateProfile(this.user.id, this.profilef.bio.value, this.profilef.website.value, this.profilef.avatar.value)
      .pipe(first())
      .subscribe({next:
        () => {
          this.successProfile = true;
          this.loading = false;
          this.errorMsg = "";
        },
        error: error => {
            this.loading = false;
            this.errorMsg = this.errorCodeService.errorMessage(error);
        }});
  }

  submitPassword() {
    this.submittedPass = true;
    this.successPassword = false;

    // stop here if form is invalid
    if (this.passwordForm.invalid) {
        return;
    }

    this.loading = true;
    this.settingService.updatePassword(this.passwordf.newPass.value, this.passwordf.repeatPass.value, this.passwordf.currentPass.value)
        .pipe(first())
        .subscribe({next:
            () => {
              this.successPassword = true;
              this.loading = false;
              this.errorPass = "";
            },
            error: error => {
                this.loading = false;
                if(error.status = 400) {
                  this.errorPass = "Invalid Password."
                }
                else {
                  this.errorPass = this.errorCodeService.errorMessage(error);
                }
            }});
    }

    createInvite() {
      this.loading = true;

      this.settingService.createInvite()
          .pipe(first())
          .subscribe({next:
              data => {
                this.loading = false;
                this.invite = `https://barrelwisdom.com/register?invite=${data['code']}`;
                this.errorInvite = "";
              },
              error: error => {
                  this.loading = false;
                  this.errorInvite = this.errorCodeService.errorMessage(error);
          }});
      }

      createSection() {
        this.submittedSection = true;
        this.successSection = false;

        // stop here if form is invalid
        if (this.sectionForm.invalid) {
            return;
        }

        this.loading = true;
        this.settingService.createSection(this.sectionf.name.value, this.sectionf.fullname.value)
            .pipe(first())
            .subscribe({next:
                () => {
                  this.successSection = true;
                  this.loading = false;
                  this.errorSection = "";
                },
                error: error => {
                    this.loading = false;
                    this.errorSection = this.errorCodeService.errorMessage(error);
                }});
        }

        loadNav(section: string) {
          this.settingService.getNavigation(section).subscribe(nav => {
            this.navigationForm.get('section').setValue(nav.section);
            this.navigationForm.get('data').setValue(nav.data);
          });
        }

        submitNav() {
          this.submittedNavigation = true;
          this.successNavigation = false;

          // stop here if form is invalid
          if (this.navigationForm.invalid) {
              return;
          }

          this.loading = true;
          this.settingService.updateNavigation(this.navigationf.section.value, this.navigationf.data.value)
              .pipe(first())
              .subscribe({next:
                  () => {
                    this.successNavigation = true;
                    this.loading = false;
                    this.errorNavigation = "";
                  },
                  error: error => {
                      this.loading = false;
                      this.errorNavigation = this.errorCodeService.errorMessage(error);
                  }});
        }
}