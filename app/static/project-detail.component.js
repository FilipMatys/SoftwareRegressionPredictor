System.register(['angular2/core', 'angular2/router', './project.service', './project-board.component', './project-settings.component', './project-git.component', './project-model.component'], function(exports_1, context_1) {
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
    var core_1, router_1, project_service_1, project_board_component_1, project_settings_component_1, project_git_component_1, project_model_component_1;
    var ProjectDetailComponent;
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
            function (project_board_component_1_1) {
                project_board_component_1 = project_board_component_1_1;
            },
            function (project_settings_component_1_1) {
                project_settings_component_1 = project_settings_component_1_1;
            },
            function (project_git_component_1_1) {
                project_git_component_1 = project_git_component_1_1;
            },
            function (project_model_component_1_1) {
                project_model_component_1 = project_model_component_1_1;
            }],
        execute: function() {
            ProjectDetailComponent = (function () {
                function ProjectDetailComponent(_router, _routeParams, _projectService) {
                    this._router = _router;
                    this._routeParams = _routeParams;
                    this._projectService = _projectService;
                }
                ProjectDetailComponent.prototype.ngOnInit = function () {
                    this.getProject(Number(this._routeParams.get('id')));
                    console.log(this._router);
                };
                ProjectDetailComponent.prototype.getProject = function (id) {
                    var _this = this;
                    this._projectService.getProject(id).subscribe(function (result) {
                        // Check if result is valid
                        if (result.isValid) {
                            _this.project = result.data;
                            _this._projectService.currentProject = _this.project;
                        }
                        else {
                            _this.errors = result.errors;
                        }
                    }, function (errors) { return _this.errors = errors; });
                };
                ProjectDetailComponent.prototype.goToProjectBlock = function (block) {
                    this._router.navigate([block]);
                };
                ProjectDetailComponent = __decorate([
                    core_1.Component({
                        selector: 'project-detail',
                        templateUrl: 'project',
                        directives: [router_1.ROUTER_DIRECTIVES]
                    }),
                    router_1.RouteConfig([
                        {
                            path: '/',
                            name: 'ProjectBoard',
                            component: project_board_component_1.ProjectBoardComponent,
                            useAsDefault: true
                        },
                        {
                            path: '/git/...',
                            name: 'ProjectGit',
                            component: project_git_component_1.ProjectGitComponent
                        },
                        {
                            path: '/model',
                            name: 'ProjectModel',
                            component: project_model_component_1.ProjectModelComponent
                        },
                        {
                            path: '/settings',
                            name: 'ProjectSettings',
                            component: project_settings_component_1.ProjectSettingsComponent
                        }
                    ]), 
                    __metadata('design:paramtypes', [router_1.Router, router_1.RouteParams, (typeof (_a = typeof project_service_1.ProjectService !== 'undefined' && project_service_1.ProjectService) === 'function' && _a) || Object])
                ], ProjectDetailComponent);
                return ProjectDetailComponent;
                var _a;
            }());
            exports_1("ProjectDetailComponent", ProjectDetailComponent);
        }
    }
});
//# sourceMappingURL=project-detail.component.js.map