require('angular');


angular.module('dockerVehicle')
    .factory('ManufacturerResource', ['$resource', function($resource) {
        return $resource('/api/manufacturers/:id/', {id:'@id'}, {
            'update': { method:'PUT' }
        });
    }]);
