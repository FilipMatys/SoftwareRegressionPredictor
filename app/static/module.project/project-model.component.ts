import { Component, OnInit } from 'angular2/core';

import { Project } from '../models/project';
import { ProjectService } from '../services/project.service';

@Component({
    selector: 'project-model',
    templateUrl: 'project_model'
})

export class ProjectModelComponent {
    public project: Project;

    constructor(private _projectService: ProjectService) {
        this.project = this._projectService.currentProject;
    }
}

