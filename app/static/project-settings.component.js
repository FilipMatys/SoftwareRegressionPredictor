System.register(['angular2/core', './project.service'], function(exports_1, context_1) {
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
    var core_1, project_service_1;
    var ProjectSettingsComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (project_service_1_1) {
                project_service_1 = project_service_1_1;
            }],
        execute: function() {
            ProjectSettingsComponent = (function () {
                function ProjectSettingsComponent(_projectService) {
                    this._projectService = _projectService;
                    this.project = this._projectService.currentProject;
                }
                ProjectSettingsComponent = __decorate([
                    core_1.Component({
                        selector: 'project-settings',
                        templateUrl: 'project_settings'
                    }), 
                    __metadata('design:paramtypes', [(typeof (_a = typeof project_service_1.ProjectService !== 'undefined' && project_service_1.ProjectService) === 'function' && _a) || Object])
                ], ProjectSettingsComponent);
                return ProjectSettingsComponent;
                var _a;
            }());
            exports_1("ProjectSettingsComponent", ProjectSettingsComponent);
        }
    }
});
//# sourceMappingURL=project-settings.component.js.map