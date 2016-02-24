import { Component, OnInit } from 'angular2/core';
import { ROUTER_DIRECTIVES } from 'angular2/router';

import { Project } from '../models/project';
import { ProjectService } from '../services/project.service';
import { RepositoryService } from '../services/repository.service';

@Component({
    selector: 'project-git-log',
    templateUrl: 'project_git_log',
    directives: [ROUTER_DIRECTIVES]
})

export class ProjectGitLogComponent implements OnInit {
    public project: Project;
    public commits: any[];
    public errors: any[];
    
    constructor(
        private _projectService: ProjectService,
        private _repositoryService: RepositoryService) {
        this.project = this._projectService.currentProject;
    }

    ngOnInit() {
        this.getLog(Number(this.project.id));
    }

    getLog(projectId: number) {
        this._repositoryService.log(projectId).subscribe(
            result => {
                // Check if result is valid
                if (result.isValid) {
                    this.commits = result.data;
                }
                // Something went wrong
                else {
                    this.errors = result.errors;
                }
            },
            errors => this.errors = errors
        );
    }
}