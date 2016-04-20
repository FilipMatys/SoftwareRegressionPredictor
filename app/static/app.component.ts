import { Component } from 'angular2/core';
import {HTTP_PROVIDERS}    from 'angular2/http';
import { RouteConfig, Router, ROUTER_DIRECTIVES, ROUTER_PROVIDERS } from 'angular2/router';

import { ApplicationAlert } from './models/alert';
import { ProjectsComponent } from './projects.component';
import { ProjectService } from './services/project.service';
import { RepositoryService } from './services/repository.service';
import { ModelService } from './services/model.service';
import { AlertService } from './services/alert.service';
import { ProjectDetailComponent } from './module.project/project-detail.component';

@Component({
    selector: 'my-app',
    templateUrl: 'frame',
    directives: [ROUTER_DIRECTIVES],
    providers: [
        ROUTER_PROVIDERS,
        HTTP_PROVIDERS,
        ProjectService,
        RepositoryService,
        ModelService,
        AlertService
    ]
})

@RouteConfig([
    {
        path: '/',
        name: 'Projects',
        component: ProjectsComponent,
        useAsDefault: true
    },
    {
        path: '/project/:id/...',
        name: 'ProjectDetail',
        component: ProjectDetailComponent
    }
])

export class AppComponent {
    private _alert: ApplicationAlert;

    constructor(private _router: Router) {
    }

    goHome() {
        this._router.navigate(['Projects']);
    }

    // Show messages via alert and 
    private _showAlert(messages: string[], message: string) {
        // Initialize alert object
        this._alert = new ApplicationAlert();
        this._alert.messages = messages;
        this._alert.message = message;
    }

    // Close alert by setting to null
    private _closeAlert() {
        this._alert = null;
    }

    // Show errors via alert object
    public showErrors(errors: string[], message: string) {
        this._showAlert(errors, message);
    }

    // Show warnings via alert object
    public showWarnings(warnings: string[], message: string) {
        this._showAlert(warnings, message);
    }

    // Show success via alert object
    public showSuccess(message: string) {
        this._showAlert([], message);
    }
}