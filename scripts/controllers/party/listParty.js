'use strict';

/**
 * @ngdoc function
 * @name horrorWarriorApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the horrorWarriorApp
 */
angular.module('horrorWarriorParty')
  .controller('listPartyCtrl', function ($scope, $http) {
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
  });
  