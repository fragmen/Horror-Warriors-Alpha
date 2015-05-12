'use strict';

/**
 * @ngdoc function
 * @name horrorWarriorApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the horrorWarriorApp
 */
angular.module('horrorWarriorApp')
  .controller('createHeroeCtrl', function ($scope,$http,$location) {
    $scope.dropHeroe = function(id_heroe){
       $http.post("../api/dropHeroe",{id_heroe:id_heroe})
            .success( function(data){
                $scope.response = JSON.parse(data);
                alert($scope.response["msg"]);
                $scope.loadHeroes();
            })
            .error( function(data){
                self.response = JSON.parse(data);
                alert($scope.response["msg"]);
            })
    }
    $scope.loadHeroes = function(){
        var id = readCookie("id");
        $http.post('../api/loadHeroes',{id_jugador:id})
                .success(function(data){
                    $scope.response =   JSON.parse(data);
                })
                .error(function(data){
                    $scope.response = JSON.parse(data);
                })
    }
    $scope.loadHeroe = function(id_heroe){
        $http.post('../api/loadHeroe',{id_heroe:id_heroe})
            .success(function (data){
                $scope.heroe = JSON.parse(data);
                $scope.nom = $scope.heroe["data"].nom;
                $scope.live = $scope.heroe["data"].live;
                $scope.agility = $scope.heroe["data"].agility;
                $scope.force = $scope.heroe["data"].force;
            })
            .error( function(data){
                
            })
    }
   
   $scope.loadHeroes();
   
    $scope.save = function(){
        var id = readCookie("id");
        $http.post('../api/createHeroe',{id_jugador:id, avatar:$scope.avatar, nom:$scope.nom, live:$scope.live, force:$scope.force, agility:$scope.agility})
        .success(function(data) {
            $scope.response = JSON.parse(data);
            alert($scope.response["msg"]);
            $scope.loadHeroes();
        })
        .error(function(data) {
            $scope.response = JSON.parse(data);
            alert($scope.response["msg"]);
    });
    }
    $scope.joinParty = function(id_heroi){
        createCookie("id_heroi",id_heroi,1);
        window.location = "PartyLayout.html#/listParty";
    }
    
  });

