System.register(['angular2/core', '../services/project.service', '../services/model.service', '../pipes/model-search.pipe'], function(exports_1, context_1) {
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
    var core_1, project_service_1, model_service_1, model_search_pipe_1;
    var ProjectModelComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (project_service_1_1) {
                project_service_1 = project_service_1_1;
            },
            function (model_service_1_1) {
                model_service_1 = model_service_1_1;
            },
            function (model_search_pipe_1_1) {
                model_search_pipe_1 = model_search_pipe_1_1;
            }],
        execute: function() {
            ProjectModelComponent = (function () {
                function ProjectModelComponent(_projectService, _modelService) {
                    this._projectService = _projectService;
                    this._modelService = _modelService;
                    this.project = this._projectService.currentProject;
                    this.term = "";
                    this.models = [];
                    this.loadModel();
                }
                ProjectModelComponent.prototype.loadModel = function () {
                    var _this = this;
                    this._modelService.load(this.project.id).subscribe(function (result) {
                        // Check if result is valid
                        if (result.isValid) {
                            _this.models = result.data;
                        }
                        else {
                            _this.errors = result.errors;
                        }
                    }, function (errors) { return _this.errors = errors; });
                };
                // Create model
                ProjectModelComponent.prototype.createModel = function () {
                    var _this = this;
                    this._modelService.create(this.project.id).subscribe(function (result) {
                        // Check if result is valid
                        if (result.isValid) {
                        }
                        else {
                            _this.errors = result.errors;
                        }
                    }, function (errors) { return _this.errors = errors; });
                };
                ProjectModelComponent = __decorate([
                    core_1.Component({
                        selector: 'project-model',
                        templateUrl: 'project_model',
                        pipes: [model_search_pipe_1.ModelSearchPipe]
                    }), 
                    __metadata('design:paramtypes', [project_service_1.ProjectService, model_service_1.ModelService])
                ], ProjectModelComponent);
                return ProjectModelComponent;
            }());
            exports_1("ProjectModelComponent", ProjectModelComponent);
        }
    }
});
//# sourceMappingURL=project-model.component.js.map