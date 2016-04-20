import { Component, OnInit } from 'angular2/core';
import {CORE_DIRECTIVES, FORM_DIRECTIVES} from 'angular2/common';
import { FILE_UPLOAD_DIRECTIVES, FileUploader } from '../node_modules/ng2-file-upload/ng2-file-upload';

import { Project } from '../models/project';
import { ProjectService } from '../services/project.service';
import { ModelService } from '../services/model.service';

@Component({
    selector: 'project-board',
    templateUrl: 'project_board',
    directives: [FILE_UPLOAD_DIRECTIVES, CORE_DIRECTIVES, FORM_DIRECTIVES]
})

export class ProjectBoardComponent {
    public project: Project;
    private uploader: FileUploader;

    constructor(
        private _projectService: ProjectService,
        private _modelService: ModelService) {

        this.project = this._projectService.currentProject;
        this.initUploader();
    }

    // Initialize uploader object and its properties
    initUploader(): void {
        // Init uploader
        this.uploader = new FileUploader({
            url: this._modelService.getFilePredictionUrl(this.project.id)
        });

        // Set uploader properties
        this.uploader.queueLimit = 1;

        // On successful upload, call this function
        this.uploader.onSuccessItem = function (item, response, status, header) {
            console.log(response);
        }
    }

    // Make prediction for file
    predictForFile(): void {
        this.uploader.queue[0].upload();
    }
}

