'use strict';

/**
 * @ngdoc function
 * @name horrorWarriorApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the horrorWarriorApp
 */
angular.module('horrorWarriorApp')
  .controller('listHeroesCtrl', function ($scope) {
    $scope.listBeast = function(){
        var id = readCookie("id");
        $http.post('../api/listHeroe',{id_jugador:id})
                .success(function(data){
                    $scope.response =   JSON.parse(data);
                })
                .error(function(data){
                    $scope.response = JSON.parse(data);
                })
    }
  });


