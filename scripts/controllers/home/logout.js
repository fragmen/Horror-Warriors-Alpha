
angular.module('horrorWarriorApp')
.controller('logoutCtrl', function ($scope, $http, $location, $rootScope) {
    $scope.logout = function(){
        
        eraseCookie("id");
        eraseCookie("nick");
        $rootScope.esJugador =false;
        $rootScope.esMaster = false;
        $rootScope.logat = false;
        $location("meuEspai");
        
    };
    $scope.logout();
    
});