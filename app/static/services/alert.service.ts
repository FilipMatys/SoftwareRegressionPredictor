import { Injectable, Inject, forwardRef } from 'angular2/core';
import { AppComponent } from '../app.component';
import { ValidationResult } from '../models/validationResult';

@Injectable()
export class AlertService {

    constructor( @Inject(forwardRef(() => AppComponent)) private _app: AppComponent) { }

    showAlert(validation: ValidationResult, failMessage: string, successMessage?: string) {
        // Not valid, so there was an error
        if (!validation.isValid) {
            this._app.showErrors(validation.errors, failMessage);
            return;
        }

        // Check for warnings
        if (validation.warnings.length > 0) {
            this._app.showWarnings(validation.warnings, successMessage);
            return;
        }

        // Show success if success message is set
        if (successMessage)
            this._app.showSuccess(successMessage);
    }
}