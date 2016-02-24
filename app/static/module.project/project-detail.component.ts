import { Component, OnInit } from 'angular2/core';
import { RouteParams,RouteConfig, Router, ROUTER_DIRECTIVES, ROUTER_PROVIDERS } from 'angular2/router';

import { Project } from '../models/project';
import { ProjectService } from '../services/project.service';
import { Observable } from 'rxjs/Observable';

import { ProjectBoardComponent } from './project-board.component';
import { ProjectSettingsComponent } from './project-settings.component';
import { ProjectGitComponent } from './project-git.component';
import { ProjectModelComponent } from './project-model.component';

@Component({
    selector: 'project-detail',
    templateUrl: 'project',
    directives: [ROUTER_DIRECTIVES]
})

@RouteConfig([
    {
        path: '/',
        name: 'ProjectBoard',
        component: ProjectBoardComponent,
        useAsDefault: true
    },
    {
        path: '/git/...',
        name: 'ProjectGit',
        component: ProjectGitComponent
    },
    {
        path: '/model',
        name: 'ProjectModel',
        component: ProjectModelComponent
    },
    {
        path: '/settings',
        name: 'ProjectSettings',
        component: ProjectSettingsComponent
    }
])

export class ProjectDetailComponent implements OnInit {

    constructor(
        private _router: Router,
        private _routeParams: RouteParams,
        private _projectService: ProjectService) {
    }

    public project: Project;
    public errors: any[];

    ngOnInit() {
        this.getProject(Number(this._routeParams.get('id')));
    }

    getProject(id: number) {
        this._projectService.getProject(id).subscribe(
            result => {
                // Check if result is valid
                if (result.isValid) {
                    this.project = result.data;
                    this._projectService.currentProject = this.project;
                }
                // Something went wrong
                else {
                    this.errors = result.errors;
                }
            },
            errors => this.errors = errors);
    }

    goToProjectBlock(block: string) {
        this._router.navigate([block]);
    }
}
