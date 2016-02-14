app.controller('ProjectCommitController', ['$scope', '$stateParams', 'RepositoryService', function ($scope, $stateParams, RepositoryService) {
    RepositoryService.getCommit($stateParams.projectId, $stateParams.hash).then(function (response) {
        $scope.commit = response.data;
    });
}]);