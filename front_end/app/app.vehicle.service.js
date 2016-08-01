require('angular');


angular.module('dockerVehicle')
    .factory('VehicleResource', ['$resource', function($resource) {
        return $resource('/api/vehicles/:id/', {id:'@id'}, {
            'update': { method:'PUT' }
        });
    }]);
