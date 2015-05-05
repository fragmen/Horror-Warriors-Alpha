'use strict';

/**
 * @ngdoc function
 * @name horrorWarriorApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the horrorWarriorApp
 */
angular.module('horrorWarriorApp')
  .controller('createBeastCtrl', function ($scope,$http) {
    $scope.loadBeast = function(){
        var id = readCookie("id");
        $http.post('../api/loadBeast',{id_master:id})
                .success(function(data){
                    $scope.response =   JSON.parse(data);
                })
                .error(function(data){
                    $scope.response = JSON.parse(data);
                })
    }
   $scope.loadBeast();
   $scope.tipus_bestia = function(){
    if($scope.avatar=="Avatar_Abominacio.jpg"){
        
    }else if($scope.avatar=="Avatar_Golem_Magma.jpg"){
        $scope.live = 40;
        $scope.defense = 20;
        $scope.force = 7;
        $scope.agility = 2;
    }else if($scope.avatar=="Avatar_Home_Llop.jpg"){
        $scope.live = 20;
        $scope.defense = 5;
        $scope.force = 5;
        $scope.agility = 2;
        
    }else if($scope.avatar=="Avatar_Orc_Guerrer.jpg"){
        $scope.live = 20;
        $scope.defense = 5;
        $scope.force = 5;
        $scope.agility = 2;
        
    }else if($scope.avatar=="Avatar_Orc_Mag.jpg"){
        $scope.live = 20;
        $scope.defense = 5;
        $scope.force = 5;
        $scope.agility = 2;
        
    }else if($scope.avatar=="Avatar_Orc_Rang.jpg"){
        $scope.live = 20;
        $scope.defense = 5;
        $scope.force = 5;
        $scope.agility = 2;
        
    }
    }
    $scope.tipus_bestia();
    $scope.save = function(){
        var id = readCookie("id");
        $http.post('../api/createBeast',{id_master:id, avatar:$scope.avatar, nom:$scope.nom, live:$scope.live, force:$scope.force, agility:$scope.agility, defense:$scope.defense})
        .success(function(data) {
            $scope.response = JSON.parse(data);
            $scope.loadBeast();
        })
        .error(function(data) {
            $scope.response = JSON.parse(data);
    });
    }
    
  });

