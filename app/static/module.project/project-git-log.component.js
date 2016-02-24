System.register(['angular2/core', 'angular2/router', '../services/project.service', '../services/repository.service'], function(exports_1, context_1) {
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
    var core_1, router_1, project_service_1, repository_service_1;
    var ProjectGitLogComponent;
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
            }],
        execute: function() {
            ProjectGitLogComponent = (function () {
                function ProjectGitLogComponent(_projectService, _repositoryService) {
                    this._projectService = _projectService;
                    this._repositoryService = _repositoryService;
                    this.project = this._projectService.currentProject;
                }
                ProjectGitLogComponent.prototype.ngOnInit = function () {
                    this.getLog(Number(this.project.id));
                };
                ProjectGitLogComponent.prototype.getLog = function (projectId) {
                    var _this = this;
                    this._repositoryService.log(projectId).subscribe(function (result) {
                        // Check if result is valid
                        if (result.isValid) {
                            _this.commits = result.data;
                        }
                        else {
                            _this.errors = result.errors;
                        }
                    }, function (errors) { return _this.errors = errors; });
                };
                ProjectGitLogComponent = __decorate([
                    core_1.Component({
                        selector: 'project-git-log',
                        templateUrl: 'project_git_log',
                        directives: [router_1.ROUTER_DIRECTIVES]
                    }), 
                    __metadata('design:paramtypes', [project_service_1.ProjectService, repository_service_1.RepositoryService])
                ], ProjectGitLogComponent);
                return ProjectGitLogComponent;
            }());
            exports_1("ProjectGitLogComponent", ProjectGitLogComponent);
        }
    }
});
//# sourceMappingURL=project-git-log.component.js.map