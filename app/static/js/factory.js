app.factory('ProjectService', function (Restangular) {
    return {
        getList: function () {
            return Restangular.all('projects').getList();
        },
        save: function (project) {
            return Restangular.all('projects').post(project);
        },
        get: function (id) {
            return Restangular.one('projects', id).get();
        }
    }
});