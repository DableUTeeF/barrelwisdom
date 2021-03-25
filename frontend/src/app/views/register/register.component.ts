import { Component, TemplateRef } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthenticationService } from '@app/services/authentication.service';
import { SettingService } from '@app/services/setting.service';
import { ErrorCodeService } from '@app/services/errorcode.service';
import { first } from 'rxjs/operators';

@Component({
  templateUrl: 'register.component.html',
  selector: 'register',
})
export class RegisterComponent {
  registerForm: FormGroup;
  loading = false;
  submitted = false;
  returnUrl: string;
  errorMsg: string;
  code: string;
  hasInvite = false;

  constructor(
    private formBuilder: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    private authenticationService: AuthenticationService,
    private settingService: SettingService,
    private errorCodeService: ErrorCodeService
    ) {
     }

    ngOnInit() {
      this.registerForm = this.formBuilder.group({
          username: ['', Validators.required],
          email: ['', [Validators.email, Validators.required]],
          password: ['', [Validators.required, Validators.minLength(8)]],
          confirmPassword: ['', [Validators.required, Validators.minLength(8)]]
      });

      if(this.route.snapshot.queryParamMap.get('invite')) {
        this.settingService.getInvite(this.route.snapshot.queryParamMap.get('invite'))
        .pipe(first())
        .subscribe(
          data => {
            if((Date.now() - Date.parse(data.date))/(1000*3600*24) < 3) {
              this.hasInvite = true;
            }
          },
          error => {
            this.hasInvite = false;
          });
      }

      this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
  }


  get f() { return this.registerForm.controls; }

  onSubmit() {
    this.submitted = true;

    if (this.registerForm.invalid) {
        return;
    }
    let success = false;
    this.loading = true;
    this.authenticationService.register(this.f.username.value, this.f.email, this.f.password.value, this.f.confirmPassword.value)
        .pipe(first())
        .subscribe(
            data => {
              success = true;
            },
            error => {
                this.loading = false;
                this.errorMsg = this.errorCodeService.errorMessage(error);
            });
      /** if(success) {
        this.authenticationService.login(this.f.username.value, this.f.password.value)
        .pipe(first())
        .subscribe(
            data => {
              this.router.navigateByUrl(this.returnUrl);
            },
            error => {
            });
      } */
  }
}