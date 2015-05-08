'use strict';

/**
 * @ngdoc function
 * @name horrorWarriorApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the horrorWarriorApp
 */
angular.module('horrorWarriorParty')
  .controller('listPartyCtrl', function ($scope, $http, $location) {
  		$scope.id_jugador = readCookie("id");
    	$scope.refreix = function (){
    		$http.get("../api/listParty")
    		.success(function (data){
    			$scope.response = (JSON.parse(data))
    		})
    		.error(function (data){
    			$scope.response = (JSON.parse(data))
    			
    		})
    	}
    	setInterval($scope.refreix, 1000);
        $scope.joinParty = function(nom,pass){
            $scope.pass = prompt("Password:");
            if($scope.pass == pass){
                   
                $scope.id = readCookie("id");
                $http.post("../api/joinParty",{nom:nom, id_jugador:$scope.id})
                    .success(function (data){
                        $scope.response = (JSON.parse(data));
                        alert($scope.response["msg"]);
                        if($scope.response["status"]=="Error3"){
                            return 0;
                        }else{
                        $location.path("viewParty");
                        }
                    })
                    .error(function (data){
                        $scope.response = (JSON.parse(data));
                        alert($scope.resposne["msg"]);

                    })
                }else{
                    alert("Error, la contrasenya no es correcta");
                }
        }
  });
  