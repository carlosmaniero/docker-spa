require('angular');

angular.module('dockerVehicle')
    .controller('vehicleController', [
        '$scope', '$resource', 'ManufacturerResource', 'VehicleResource',
        function($scope, $resource, ManufacturerResource, VehicleResource) {
            $scope.vehicle = new VehicleResource();
            $scope.list = VehicleResource.query();
            $scope.manufacturers = ManufacturerResource.query();

            $scope.edit = function(item){
                $scope.vehicle = item;
            };

            $scope.reload = function(){
                $scope.list = VehicleResource.query();
                $scope.vehicle = new VehicleResource();
            };

            $scope.save = function(){
                if($scope.vehicle.id){
                    var $id = $scope.vehicle.id;
                    VehicleResource.update({ id:$id }, $scope.vehicle, $scope.reload);
                }else{
                    $scope.vehicle.$save($scope.reload);
                }
            }

            $scope.delete = function(vehicle){
                vehicle.$delete($scope.reload);
            }
    }]);
