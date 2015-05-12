'use strict';

/**
 * @ngdoc function
 * @name horrorWarriorApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the horrorWarriorApp
 */
angular.module('horrorWarriorApp')
  .controller('listBeastCtrl', function ($scope) {
    $scope.listBeast = function(){
        var id = readCookie("id");
        $http.post('../api/listBeast',{id_master:id})
                .success(function(data){
                    $scope.response =   JSON.parse(data);
                })
                .error(function(data){
                    $scope.response = JSON.parse(data);
                })
    }
  });


