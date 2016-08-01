require('angular');

angular.module('dockerVehicle')
    .controller('searchController', [
        '$scope', 'searchFilters', 'SearchService',
        function($scope, searchFilters, SearchService) {
            $scope.filters = searchFilters;
            $scope.query = "";
            $scope.query_filters = {}
            $scope.results = [];

            $scope.search = function(){
                SearchService($scope.query, $scope.query_filters, function(data){
                    $scope.results = data;
                });
            }
        }]);
