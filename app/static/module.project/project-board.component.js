System.register(['angular2/core', 'angular2/common', '../node_modules/ng2-file-upload/ng2-file-upload', '../services/project.service', '../services/model.service', '../services/alert.service'], function(exports_1, context_1) {
    "use strict";
    var __moduleName = context_1 && context_1.id;
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var core_1, common_1, ng2_file_upload_1, project_service_1, model_service_1, alert_service_1;
    var ProjectBoardComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (common_1_1) {
                common_1 = common_1_1;
            },
            function (ng2_file_upload_1_1) {
                ng2_file_upload_1 = ng2_file_upload_1_1;
            },
            function (project_service_1_1) {
                project_service_1 = project_service_1_1;
            },
            function (model_service_1_1) {
                model_service_1 = model_service_1_1;
            },
            function (alert_service_1_1) {
                alert_service_1 = alert_service_1_1;
            }],
        execute: function() {
            ProjectBoardComponent = (function () {
                function ProjectBoardComponent(_projectService, _modelService, _alertService) {
                    this._projectService = _projectService;
                    this._modelService = _modelService;
                    this._alertService = _alertService;
                    this.project = this._projectService.currentProject;
                    this._hasModel = this._modelService.hasModel;
                    this.initUploader();
                }
                // Initialize uploader object and its properties
                ProjectBoardComponent.prototype.initUploader = function () {
                    var _this = this;
                    // Init uploader
                    this.uploader = new ng2_file_upload_1.FileUploader({
                        url: this._modelService.getFilePredictionUrl(this.project.id)
                    });
                    // Set uploader properties
                    this.uploader.queueLimit = 1;
                    // On successful upload, call this function
                    this.uploader.onSuccessItem = function (item, response, status, header) {
                        _this._alertService.showAlert(JSON.parse(response), "Failed to make prediction", null);
                    };
                };
                // Make prediction for file
                ProjectBoardComponent.prototype.predictForFile = function () {
                    this.uploader.queue[0].upload();
                };
                ProjectBoardComponent = __decorate([
                    core_1.Component({
                        selector: 'project-board',
                        templateUrl: 'project_board',
                        directives: [ng2_file_upload_1.FILE_UPLOAD_DIRECTIVES, common_1.CORE_DIRECTIVES, common_1.FORM_DIRECTIVES]
                    }), 
                    __metadata('design:paramtypes', [project_service_1.ProjectService, model_service_1.ModelService, alert_service_1.AlertService])
                ], ProjectBoardComponent);
                return ProjectBoardComponent;
            }());
            exports_1("ProjectBoardComponent", ProjectBoardComponent);
        }
    }
});
//# sourceMappingURL=project-board.component.js.map