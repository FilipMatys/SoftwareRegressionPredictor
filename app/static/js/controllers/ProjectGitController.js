app.controller('ProjectGitController', ['$scope', 'RepositoryService', function ($scope, RepositoryService) {
    //RepositoryService.exists($scope.project.id);
    RepositoryService.log($scope.project.id).then(function(result){
        $scope.commits = result.data;
    });
}]);