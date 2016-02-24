import { Component, OnInit } from 'angular2/core';

import { Project } from '../models/project';
import { ProjectService } from '../services/project.service';

@Component({
    selector: 'project-settings',
    templateUrl: 'project_settings'
})

export class ProjectSettingsComponent {
    public project: Project;

    constructor(private _projectService: ProjectService) {
        this.project = this._projectService.currentProject;
    }
}

