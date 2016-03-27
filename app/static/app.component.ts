import { Component } from 'angular2/core';
import {HTTP_PROVIDERS}    from 'angular2/http';
import { RouteConfig, Router, ROUTER_DIRECTIVES, ROUTER_PROVIDERS } from 'angular2/router';

import { ProjectsComponent } from './projects.component';
import { ProjectService } from './services/project.service';
import { RepositoryService } from './services/repository.service';
import { ModelService } from './services/model.service';
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
        ModelService
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
    constructor(private _router: Router) {}

    goHome() {
        this._router.navigate(['Projects']);
    }
}