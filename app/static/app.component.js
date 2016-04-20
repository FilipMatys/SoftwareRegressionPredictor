System.register(['angular2/core', 'angular2/http', 'angular2/router', './models/alert', './projects.component', './services/project.service', './services/repository.service', './services/model.service', './services/alert.service', './module.project/project-detail.component'], function(exports_1, context_1) {
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
    var core_1, http_1, router_1, alert_1, projects_component_1, project_service_1, repository_service_1, model_service_1, alert_service_1, project_detail_component_1;
    var AppComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (http_1_1) {
                http_1 = http_1_1;
            },
            function (router_1_1) {
                router_1 = router_1_1;
            },
            function (alert_1_1) {
                alert_1 = alert_1_1;
            },
            function (projects_component_1_1) {
                projects_component_1 = projects_component_1_1;
            },
            function (project_service_1_1) {
                project_service_1 = project_service_1_1;
            },
            function (repository_service_1_1) {
                repository_service_1 = repository_service_1_1;
            },
            function (model_service_1_1) {
                model_service_1 = model_service_1_1;
            },
            function (alert_service_1_1) {
                alert_service_1 = alert_service_1_1;
            },
            function (project_detail_component_1_1) {
                project_detail_component_1 = project_detail_component_1_1;
            }],
        execute: function() {
            AppComponent = (function () {
                function AppComponent(_router) {
                    this._router = _router;
                }
                AppComponent.prototype.goHome = function () {
                    this._router.navigate(['Projects']);
                };
                // Show messages via alert and 
                AppComponent.prototype._showAlert = function (messages, message) {
                    // Initialize alert object
                    this._alert = new alert_1.ApplicationAlert();
                    this._alert.messages = messages;
                    this._alert.message = message;
                };
                // Close alert by setting to null
                AppComponent.prototype._closeAlert = function () {
                    this._alert = null;
                };
                // Show errors via alert object
                AppComponent.prototype.showErrors = function (errors, message) {
                    this._showAlert(errors, message);
                };
                // Show warnings via alert object
                AppComponent.prototype.showWarnings = function (warnings, message) {
                    this._showAlert(warnings, message);
                };
                // Show success via alert object
                AppComponent.prototype.showSuccess = function (message) {
                    this._showAlert([], message);
                };
                AppComponent = __decorate([
                    core_1.Component({
                        selector: 'my-app',
                        templateUrl: 'frame',
                        directives: [router_1.ROUTER_DIRECTIVES],
                        providers: [
                            router_1.ROUTER_PROVIDERS,
                            http_1.HTTP_PROVIDERS,
                            project_service_1.ProjectService,
                            repository_service_1.RepositoryService,
                            model_service_1.ModelService,
                            alert_service_1.AlertService
                        ]
                    }),
                    router_1.RouteConfig([
                        {
                            path: '/',
                            name: 'Projects',
                            component: projects_component_1.ProjectsComponent,
                            useAsDefault: true
                        },
                        {
                            path: '/project/:id/...',
                            name: 'ProjectDetail',
                            component: project_detail_component_1.ProjectDetailComponent
                        }
                    ]), 
                    __metadata('design:paramtypes', [router_1.Router])
                ], AppComponent);
                return AppComponent;
            }());
            exports_1("AppComponent", AppComponent);
        }
    }
});
//# sourceMappingURL=app.component.js.map