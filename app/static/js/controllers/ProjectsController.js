app.controller('ProjectsController', ['$scope', 'ProjectService', function ($scope, ProjectService) {
    ProjectService.getList();
}]);