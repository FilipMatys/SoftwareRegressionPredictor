app.factory('ProjectService', function (Restangular) {
    return {
        getList: function () {
            return Restangular.one('projects').get();
        },
        get: function (id) {
            return Restangular.one('projects', id).get();
        }
    }
});

app.factory('GitService', function (Restangular) {
    return {
        clone: function (id) {
            return Restangular.one('git', id).get();
        }
    }
});