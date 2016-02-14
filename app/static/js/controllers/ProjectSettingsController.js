app.controller('ProjectSettingsController', ['$scope', 'RepositoryService', function ($scope, RepositoryService) {
    // Clone project
    $scope.cloneProject = function () {
        RepositoryService.clone($scope.project.id);
    }
}]);