import { Component, OnInit } from 'angular2/core';

import { Project } from '../models/project';
import { ProjectService } from '../services/project.service';
import { RepositoryService } from '../services/repository.service';

@Component({
    selector: 'project-settings',
    templateUrl: 'project_settings'
})

export class ProjectSettingsComponent {
    public project: Project;
    private _repositoryExists: boolean;

    constructor(private _projectService: ProjectService, private _repositoryService: RepositoryService) {
        this.project = this._projectService.currentProject;
        this._repositoryExists = this._repositoryService.repositoryExits;
    }
}

