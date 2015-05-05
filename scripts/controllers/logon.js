
angular.module('horrorWarriorApp')
.controller('logonCtrl', function ($scope, $http) {
    $scope.myData = {};
    $scope.myData.login = function() {
        $http.post('../api/login',{nick: $scope.nick, password:$scope.password, master:$scope.master}).
        success(function(data) {
        // this callback will be called asynchronously
        // when the response is availablea
        $scope.response = JSON.parse(data);
        alert($scope.response["status"]);
        
        }).
  error(function(data) {

    // called asynchronously if an error occurs
    // or server returns response with an error status.
    $scope.response = JSON.parse(data);
    alert($scope.response["status"]);
  });
    }                   
});