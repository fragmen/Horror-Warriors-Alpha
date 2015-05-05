angular
  .module('horrorWarriorApp', ["ngRoute"]).config(

function direccions($routeProvider){
    $routeProvider
        .when("/", {
                controller: "homeCtrl",
                controllerAs: "homeCtrl",
                templateUrl: "views/home.html"
        })
        .when("/login", {
                controller: "loginCtrl",
                controllerAs: "loginCtrl",
                templateUrl: "views/home/login.html"
            })
        .when("/meuEspai", {
                controller: "meuEspaiCtrl",
                controllerAs: "meuEspaiCtrl",
                templateUrl: "views/home/meuEspai.html"
            })
        .when("/logon", {
                controller: "logonCtrl",
                controllerAs: "logonCtrl",
                templateUrl: "views/logon.html"
            })
        .when("/party", {
                controller: "partyCtrl",
                controllerAs: "partyCtrl",
                templateUrl: "views/party.html"

        })
        .when("/createMaps", {
                controller: "createMapsCtrl",
                controllerAs: "createMapsCtrl",
                templateUrl: "views/maps/createMaps.html"

        })
        .when("/createBeast", {
                controller: "createBeastCtrl",
                controllerAs: "createBeastCtrl",
                templateUrl: "views/beast/createBeast.html"

        })
        .when("/listBeast",{
                controller: "listBeastCtrl",
                controllerAs: "listBeastCtrl",
                templateUrl: "views/beast/listBeast.html"
        })
        .when("/gameView",{
                controller: "gameViewCtrl",
                controllerAs: "gameViewCtrl",
                templateUrl: "views/game/gameView.html"
        })
        .otherwise({
        redirectTo: '/'
      })
});