angular
  .module('horrorWarriorParty', ["ngRoute"]).config(

function direccions($routeProvider){
    $routeProvider
		.when("/", {
                controller: "sessioPartyCtrl",
                controllerAs: "sessioPartyCtrl",
                templateUrl: "views/party/sessioParty.html"
        })
        .when("/createParty", {
                controller: "createPartyCtrl",
                controllerAs: "createPartyCtrl",
                templateUrl: "views/party/createParty.html"
            })
        .when("/listParty", {
                controller: "listPartyCtrl",
                controllerAs: "listPartyCtrl",
                templateUrl: "views/party/listParty.html"
            })
        .when("/viewParty", {
            controller: "viewPartyCtrl",
            controllerAs: "viewPartyCtrl",
            templateUrl: "views/party/viewParty.html"
        })
        
        .otherwise({
        redirectTo: '/'
      })

});