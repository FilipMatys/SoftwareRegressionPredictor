app.controller('ProjectSettingsController', ['$scope', 'GitService', function ($scope, GitService) {
    // Clone project
    $scope.cloneProject = function () {
        GitService.clone($scope.project.id);
    }
}]);