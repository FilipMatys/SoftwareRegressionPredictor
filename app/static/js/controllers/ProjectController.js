app.controller('ProjectController', ['$scope', 'projectRequest', 'ProjectService', function ($scope, projectRequest, ProjectService) {
    // Assign project into variable
    $scope.project = projectRequest.data;
}]);