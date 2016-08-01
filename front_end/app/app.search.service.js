require('angular');


angular.module('dockerVehicle')
    .factory('searchFilters', ['$http', function($http) {
        var filters = {
            'loading': true
        }
        $http.get('/api/index/filters/').then(function(response){
            if(response.status == 200){
                angular.extend(filters, response.data)
                filters.loading = false;
            }
        });

        return filters;
    }]);

angular.module('dockerVehicle')
    .factory('SearchService', ['$http', function($http) {
        return function(query, filters, successCallback, failCallback){
            strFilters = JSON.stringify(filters)
            return $http.get('/api/index/search/?q=' + query + '&filters=' + strFilters).then(
                function(response){
                    return successCallback(response.data);
                }, failCallback
            )
        }
    }]);
