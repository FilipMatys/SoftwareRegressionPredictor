System.register(['angular2/core', 'angular2/router', './module.project/project-git-log.component', './module.project/project-git-commit.component'], function(exports_1, context_1) {
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
    var core_1, router_1, project_git_log_component_1, project_git_commit_component_1;
    var ProjectGitComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (router_1_1) {
                router_1 = router_1_1;
            },
            function (project_git_log_component_1_1) {
                project_git_log_component_1 = project_git_log_component_1_1;
            },
            function (project_git_commit_component_1_1) {
                project_git_commit_component_1 = project_git_commit_component_1_1;
            }],
        execute: function() {
            ProjectGitComponent = (function () {
                function ProjectGitComponent() {
                }
                ProjectGitComponent = __decorate([
                    core_1.Component({
                        selector: 'project-git',
                        templateUrl: 'project_git',
                        directives: [router_1.ROUTER_DIRECTIVES]
                    }),
                    router_1.RouteConfig([
                        {
                            path: '/',
                            name: 'ProjectGitLog',
                            component: project_git_log_component_1.ProjectGitLogComponent,
                            useAsDefault: true
                        },
                        {
                            path: '/commit/:hash',
                            name: 'ProjectGitCommit',
                            component: project_git_commit_component_1.ProjectGitCommitComponent
                        }
                    ]), 
                    __metadata('design:paramtypes', [])
                ], ProjectGitComponent);
                return ProjectGitComponent;
            }());
            exports_1("ProjectGitComponent", ProjectGitComponent);
        }
    }
});
//# sourceMappingURL=project-git.component.js.map