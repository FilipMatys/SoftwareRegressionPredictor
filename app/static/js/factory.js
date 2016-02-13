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