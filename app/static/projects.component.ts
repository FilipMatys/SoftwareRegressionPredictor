import { Component, OnInit } from 'angular2/core';
import { Router } from 'angular2/router';

import { Project } from './models/project'
import { ProjectService } from './services/project.service'

@Component({
    selector: 'projects',
    templateUrl: 'projects'
})

export class ProjectsComponent implements OnInit {

    constructor(
        private _router: Router,
        private _projectService: ProjectService) {
    }

    public projects: Project[];
    public errors: any[];

    ngOnInit() {
        this.getProjects();
    }

    goToDetail(selectedId: number) {
        this._router.navigate(['ProjectDetail', { id: selectedId }]);
    }

    getProjects() {
        this._projectService.getProjects().subscribe(
            result => {
                // Check if result is valid
                if (result.isValid) {
                    this.projects = result.data;
                }
                // Something went wrong
                else {
                    this.errors = result.errors;
                }
            },
            errors => this.errors = errors);
    }
}
