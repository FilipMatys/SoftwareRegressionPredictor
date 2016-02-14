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

app.factory('RepositoryService', function (Restangular) {
    return {
        clone: function (id) {
            return Restangular.one('repository', id).one('clone').get();
        },
        exists: function (id) {
            return Restangular.one('repository', id).one('exists').get();
        },
        log: function (id) {
            return Restangular.one('repository', id).one('log').get();
        },
        getCommit: function (id, hash) {
            return Restangular.one('repository', id).one('commit', hash).get();
        }
    }
});