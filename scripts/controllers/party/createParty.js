'use strict';

/**
 * @ngdoc function
 * @name horrorWarriorApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the horrorWarriorApp
 */
angular.module('horrorWarriorParty')
  .controller('createPartyCtrl', function ($scope, $http, $rootScope,$location) {
  	$scope.online = function(nomParty, estatParty){
  		$http.post("../api/onlineParty", {nom:nomParty,estat:estatParty})
  			.success(function(data){
  				$scope.response = JSON.parse(data)
  				
  				alert("Ara l'estat acutal de la partida online ="+$scope.response["estat"])
  				if($scope.response["estat"]=="True"){
  					$scope.styleOnline="color:green";
  				}else{
  					$scope.styleOnline="color:red";
  				}
  				$scope.refresca()
  			})
  			.error( function (data){
				alert($scope.response["msg"])
  			})
  	}
    $scope.save = function(){
    	$scope.master_id = readCookie("id");
    	$http.post("../api/createParty",{master_id:$scope.master_id,nom:$scope.nom, pass:$scope.pass, maxper:$scope.maxper, idioma:$scope.idioma})
    	.success( function(data){
    		 $scope.response = JSON.parse(data);
    		 $scope.refresca();
    		 alert($scope.response["msg"])
    	})
    	.error( function(data){
    		$scope.response = "Error en el POST amb json al webservice";
    		alert($scope.response["status"]+$scope.response["msg"])
    	});
    };
    $scope.refresca = function(){
    	var id = readCookie("id");
        $http.post('../api/loadPartys',{id_jugador:id})
                .success(function(data){
                    $scope.partides =   JSON.parse(data);
                })
                .error(function(data){
                    $scope.response = JSON.parse(data);
                    alert($scope.response["msg"])
                })
    }
    $scope.joinParty = function(nom){
        $rootScope.nomParty = nom;
        $location.path("viewParty");
    }
    $scope.refresca();
    
  });






