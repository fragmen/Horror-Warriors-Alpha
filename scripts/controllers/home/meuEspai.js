'use strict';


angular.module('horrorWarriorApp')
  .controller('meuEspaiCtrl', function ($scope, $rootScope, $http, $location) {
    $scope.nick = readCookie("nick");
    $scope.id = readCookie("id");
    var entrada = function(){ $http.post("../api/esMaster",{id:$scope.id}).
        success( function (data){
            data = JSON.parse(data);
            if(data["master"]==true){
                $rootScope.esMaster = true;
                $rootScope.esJugador = false;
                $rootScope.logat=true;
                
            }else if(data["master"]==false){
                $rootScope.esMaster = false;
                $rootScope.esJugador = true;
                $rootScope.logat=true;
                $location.path("createHeroe");
            }
            
      }).error(function (data){

            console.log("Error de conexio a la prova del master");
      });
    };
    entrada();
  });
  