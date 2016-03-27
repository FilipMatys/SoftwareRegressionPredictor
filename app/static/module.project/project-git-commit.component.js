System.register(['angular2/core', 'angular2/router', '../services/project.service', '../services/repository.service', '../services/model.service'], function(exports_1, context_1) {
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
    var core_1, router_1, project_service_1, repository_service_1, model_service_1;
    var ProjectGitCommitComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (router_1_1) {
                router_1 = router_1_1;
            },
            function (project_service_1_1) {
                project_service_1 = project_service_1_1;
            },
            function (repository_service_1_1) {
                repository_service_1 = repository_service_1_1;
            },
            function (model_service_1_1) {
                model_service_1 = model_service_1_1;
            }],
        execute: function() {
            ProjectGitCommitComponent = (function () {
                function ProjectGitCommitComponent(_routeParams, _projectService, _modelService, _repositoryService) {
                    this._routeParams = _routeParams;
                    this._projectService = _projectService;
                    this._modelService = _modelService;
                    this._repositoryService = _repositoryService;
                    this.showLinesOfCode = true;
                    this.showCodeAnalysis = true;
                    this.project = this._projectService.currentProject;
                    this.toolsPanel = {
                        show: 'All'
                    };
                    this.changes = [];
                }
                ProjectGitCommitComponent.prototype.ngOnInit = function () {
                    this.getLog(Number(this.project.id), this._routeParams.get('hash'));
                    this.makePrediction(Number(this.project.id), this._routeParams.get('hash'));
                };
                /**
                 * Show items based on selected value
                 * @param state Selected state
                 * @param label Label of selected state
                 */
                ProjectGitCommitComponent.prototype.showToolItem_itemSelected = function (state, label) {
                    switch (state) {
                        case 'changes':
                            this.showLinesOfCode = true;
                            this.showCodeAnalysis = false;
                            console.log('Changes');
                            break;
                        case 'analysis':
                            this.showLinesOfCode = false;
                            this.showCodeAnalysis = true;
                            console.log("Analysis");
                            break;
                        case 'all':
                            this.showLinesOfCode = true;
                            this.showCodeAnalysis = true;
                            console.log("All");
                            break;
                    }
                    // Set label
                    this.toolsPanel.show = label;
                };
                ProjectGitCommitComponent.prototype.makePrediction = function (projectId, hash) {
                    var _this = this;
                    this._modelService.predict(projectId, hash).subscribe(function (result) {
                        // Check if result is valid
                        if (result.isValid) {
                            _this.changes = result.data;
                        }
                        else {
                            _this.errors = result.errors;
                        }
                    }, function (errors) { return _this.errors = errors; });
                };
                ProjectGitCommitComponent.prototype.getLog = function (projectId, hash) {
                    var _this = this;
                    this._repositoryService.getCommit(projectId, hash).subscribe(function (result) {
                        // Check if result is valid
                        if (result.isValid) {
                            _this.commit = result.data;
                            // Map changes object into list
                            for (var index = 0; index < _this.commit.diff.files.length; index++) {
                                _this.commit.diff.files[index].added.changes = _this.mapObjectToList(_this.commit.diff.files[index].added.changes);
                                _this.commit.diff.files[index].removed.changes = _this.mapObjectToList(_this.commit.diff.files[index].removed.changes);
                            }
                        }
                        else {
                            _this.errors = result.errors;
                        }
                    }, function (errors) { return _this.errors = errors; });
                };
                /**
                 * Map object into array
                 * @param object
                 */
                ProjectGitCommitComponent.prototype.mapObjectToList = function (object) {
                    var array = [];
                    // Iterate through each key
                    for (var key in object) {
                        array.push({
                            name: key,
                            value: object[key]
                        });
                    }
                    return array;
                };
                ProjectGitCommitComponent = __decorate([
                    core_1.Component({
                        selector: 'project-git-commit',
                        templateUrl: 'project_git_commit'
                    }), 
                    __metadata('design:paramtypes', [router_1.RouteParams, project_service_1.ProjectService, model_service_1.ModelService, repository_service_1.RepositoryService])
                ], ProjectGitCommitComponent);
                return ProjectGitCommitComponent;
            }());
            exports_1("ProjectGitCommitComponent", ProjectGitCommitComponent);
        }
    }
});
//# sourceMappingURL=project-git-commit.component.js.map