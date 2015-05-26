'use strict';

angular.module('horrorWarriorParty')
  .controller('viewPartyCtrl', function ($scope, $rootScope, $http) {
    $scope.refresca = function(){
      $scope.id = readCookie("id");
      $scope.nomParty = $rootScope.nomParty;
      $http.post("../api/viewParty",{nomParty:$scope.nomParty})
              .success( function(data){
                  $scope.response = (JSON.parse(data));-
                  console.log($scope.response["herois"]);
               })
               .error( function(data){
                  $scope.response2 = (JSON.parse(data));
               });
      $http.post("../api/esMaster",{id:$scope.id}).
        success( function (data){
            data = JSON.parse(data);
            if(data["master"]==true){
                $rootScope.esMaster = true;
                $rootScope.esJugador = false;
                
            }else if(data["master"]==false){
                $rootScope.esMaster = false;
                $rootScope.esJugador = true;
                $location.path("createHeroe");
            }
            }).error(function (data){

            console.log("Error de conexio a la prova del master");
      });
    };
    setInterval($scope.refresca, 3000);
                  
      });
