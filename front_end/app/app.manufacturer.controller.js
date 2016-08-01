require('angular');

angular.module('dockerVehicle')
    .controller('manufacturerController', ['$scope', '$resource', 'ManufacturerResource', function($scope, $resource, ManufacturerResource) {
        $scope.manufacturer = new ManufacturerResource();
        $scope.list = ManufacturerResource.query();

        $scope.edit = function(item){
            $scope.manufacturer = item;
        };

        $scope.reload = function(){
            $scope.list = ManufacturerResource.query();
            $scope.manufacturer = new ManufacturerResource();
        };

        $scope.save = function(){
            if($scope.manufacturer.id){
                var $id = $scope.manufacturer.id;
                ManufacturerResource.update({ id:$id }, $scope.manufacturer, $scope.reload);
            }else{
                $scope.manufacturer.$save($scope.reload);
            }
        }

        $scope.delete = function(manufacturer){
            manufacturer.$delete($scope.reload);
        }
    }]);
