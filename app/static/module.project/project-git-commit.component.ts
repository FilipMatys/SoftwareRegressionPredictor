import { Component, OnInit } from 'angular2/core';
import { RouteParams } from 'angular2/router';

import { Project } from '../models/project';
import { ProjectService } from '../services/project.service';
import { RepositoryService } from '../services/repository.service';

@Component({
    selector: 'project-git-commit',
    templateUrl: 'project_git_commit'
})


export class ProjectGitCommitComponent implements OnInit {
    public project: Project;
    public commit: any;
    public errors: string[];

    constructor(
        private _routeParams: RouteParams,
        private _projectService: ProjectService,
        private _repositoryService: RepositoryService) {
        this.project = this._projectService.currentProject;
    }

    ngOnInit() {
        this.getLog(Number(this.project.id), this._routeParams.get('hash'));
    }

    getLog(projectId: number, hash: string) {
        this._repositoryService.getCommit(projectId, hash).subscribe(
            result => {
                // Check if result is valid
                if (result.isValid) {
                    this.commit = result.data;
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