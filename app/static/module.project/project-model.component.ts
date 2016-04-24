import { Component, OnInit } from 'angular2/core';

import { Project } from '../models/project';
import { ProjectService } from '../services/project.service';
import { PollingService } from '../services/polling.service';
import { ModelService } from '../services/model.service';
import { ModelSearchPipe } from '../pipes/model-search.pipe';

import {Observable}     from 'rxjs/Observable';

@Component({
    selector: 'project-model',
    templateUrl: 'project_model',
    pipes: [ModelSearchPipe]
})

export class ProjectModelComponent {
    public project: Project;
    public models: any[];
    public errors: any[];
    public term: string;

    constructor(private _projectService: ProjectService, private _modelService: ModelService) {
        this.project = this._projectService.currentProject;
        this.term = "";
        this.models = [];
        this.loadModel();
    }

    loadModel() {
        this._modelService.load(this.project.id).subscribe(
            result => {
                // Check if result is valid
                if (result.isValid) {
                    this.models = result.data
                }
                // Something went wrong
                else {
                    this.errors = result.errors;
                }
            },
            errors => this.errors = errors);
    }

    // Create model
    createModel() {
        this._modelService.create(this.project.id).subscribe(
            result => {
                // Check if result is valid
                if (result.isValid) {
                    this.loadModel();
                    this._modelService.hasModel = true;
                }
                // Something went wrong
                else {
                    this.errors = result.errors;
                }
            },
            errors => this.errors = errors);
    }
}

