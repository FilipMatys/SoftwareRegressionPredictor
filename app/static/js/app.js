var app = angular.module('SWRP', [
    'ui.router',
    'restangular'
]);

app.config(function(RestangularProvider) {
    RestangularProvider.setBaseUrl('/api');
});

app.config(function ($stateProvider, $urlRouterProvider) {
    // Default page
    $urlRouterProvider.otherwise('/');

    // Define states
    $stateProvider
        // Dashboard page
        .state('dashboard', {
            url: '/',
            templateUrl: 'dashboard',
            controller: 'DashboardController'
        })
        // Projects page
        .state('projects', {
            url: '/projects',
            templateUrl: 'projects',
            controller: 'ProjectsController'
        })
});