app.controller('ProjectsController', ['$scope', 'projectsRequest', 'ProjectService', function ($scope, projectsRequest, ProjectService) {
    // Assign projects into variable
    $scope.projects = projectsRequest.data;
}]);