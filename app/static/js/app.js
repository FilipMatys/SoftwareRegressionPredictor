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
        // Projects page
        .state('projects', {
            url: '/',
            templateUrl: 'projects',
            controller: 'ProjectsController',
            resolve: {
                projectsRequest: function (ProjectService) {
                    return ProjectService.getList();
                }
            }
        })
        .state('project', {
            url: '/project/:projectId',
            templateUrl: 'project',
            controller: 'ProjectController',
            abstract: true,
            resolve: {
                projectRequest: function (ProjectService, $stateParams) {
                    return ProjectService.get($stateParams.projectId);
                }
            }
        })
        .state('project.board', {
            url: '',
            templateUrl: 'project_board',
            controller: 'ProjectBoardController',
        })
        .state('project.git', {
            url: '/git',
            templateUrl: 'project_git',
            controller: 'ProjectGitController',
        })
        .state('project.commit', {
            url: '/git/:hash',
            templateUrl: 'commit',
            controller: 'ProjectCommitController',
        })
        .state('project.model', {
            url: '/model',
            templateUrl: 'project_model',
            controller: 'ProjectModelController',
        })
        .state('project.settings', {
            url: '/settings',
            templateUrl: 'project_settings',
            controller: 'ProjectSettingsController',
        })
});