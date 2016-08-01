require('angular')


angular.
  module('dockerVehicle').
  config(['$locationProvider', '$routeProvider', '$resourceProvider',
    function config($locationProvider, $routeProvider, $resourceProvider) {
      $resourceProvider.defaults.stripTrailingSlashes = false;
      $locationProvider.hashPrefix('!');

      $routeProvider.
        when('/home', {
          templateUrl: 'templates/search.html',
          controller: 'searchController'
        }).
        when('/manufacturer', {
          templateUrl: 'templates/manufacturer.html',
          controller: 'manufacturerController'
        }).
        when('/vehicles', {
          templateUrl: 'templates/vehicles.html',
          controller: 'vehicleController'
        }).
        otherwise('/home');
    }
  ]);
