
angular.module('horrorWarriorApp')
.controller('loginCtrl', function ($scope, $http,$rootScope,$location) {
    $scope.myData = {};
    $scope.myData.login = function() {
        $http.post('../api/login',{nick: $scope.nick, password:$scope.password}).
        success(function(data) {
            $scope.response = JSON.parse(data);
            if($scope.response["uid"]!=null){
                $rootScope.jugador = $scope.response["uid"];
                createCookie("nick",$scope.response["nick"],1);
                createCookie("id",$scope.response["uid"],1);
                $location.path("meuEspai");
            };
        })
        .error(function(data) {
            $scope.response = JSON.parse(data);
    });
}
});