'use strict';

angular.module('horrorWarriorApp')
  .controller('createMapsCtrl', function ($scope, $http) {
      $scope.background = "forest.jpg";
      $scope.id = readCookie("id");
      $scope.saveMap = function (){ $http.post("../api/createMap",{id:$scope.id, mapName:$scope.mapName, col:$scope.col, fil:$scope.fil, background:$scope.background})
        .success(function (data){
            $scope.response = JSON.parse(data);
      })
        .error( function(data){
            $scope.response = JSON.parse(data);
      });
  };
      $scope.canvasReady = function(){
        var c = document.getElementById("myCanvas");
        var ctx = c.getContext("2d");
        $scope.fons = $scope.background;
        var i,j=0;
        for(i=0;i<= $scope.fil;i++){
            for (j=0;j<=$scope.col;j++){
                ctx.rect(i*50,j*50,50,50);
                console.log("i="+i,"j="+j);
                console.log($scope.background);

            };
          };
        ctx.stroke();
            

        console.log("Estas al canvas");
  };
  $scope.fons = "{'background-image':'url(/dist/images/backgrounds/"+$scope.background+")'}";
});

