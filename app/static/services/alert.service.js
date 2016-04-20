System.register(['angular2/core', '../app.component'], function(exports_1, context_1) {
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
    var __param = (this && this.__param) || function (paramIndex, decorator) {
        return function (target, key) { decorator(target, key, paramIndex); }
    };
    var core_1, app_component_1;
    var AlertService;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (app_component_1_1) {
                app_component_1 = app_component_1_1;
            }],
        execute: function() {
            AlertService = (function () {
                function AlertService(_app) {
                    this._app = _app;
                }
                AlertService.prototype.showAlert = function (validation, failMessage, successMessage) {
                    // Not valid, so there was an error
                    if (!validation.isValid) {
                        this._app.showErrors(validation.errors, failMessage);
                        return;
                    }
                    // Check for warnings
                    if (validation.warnings.length > 0) {
                        this._app.showWarnings(validation.warnings, successMessage);
                        return;
                    }
                    // Show success if success message is set
                    if (successMessage)
                        this._app.showSuccess(successMessage);
                };
                AlertService = __decorate([
                    core_1.Injectable(),
                    __param(0, core_1.Inject(core_1.forwardRef(function () { return app_component_1.AppComponent; }))), 
                    __metadata('design:paramtypes', [app_component_1.AppComponent])
                ], AlertService);
                return AlertService;
            }());
            exports_1("AlertService", AlertService);
        }
    }
});
//# sourceMappingURL=alert.service.js.map