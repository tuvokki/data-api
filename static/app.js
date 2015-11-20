var myApp = angular.module('myApp', ['ui.router', 'ui.bootstrap']);

myApp.factory('Slides', function($http) {
  var getSlides = function getSlides() {
    return   $http({
    method: 'GET',
    url: '/slides/'
    })
  }
  return {
    getSlides: getSlides
  };

});

myApp.controller('CarouselDemoCtrl', function($log, Slides) {
  var self = this;
  this.myInterval = 0; //disable autoscrolling
  this.noWrapSlides = true; //stop at the last slide
  
  Slides.getSlides().then(function(slides) {
    $log.debug(slides.data.slides);
    self.slides = slides.data.slides;
  }, function errorCallback(response) {
    $log.error('no slides: ', response)
  });
})

myApp.config(function($stateProvider, $urlRouterProvider) {
  //
  // For any unmatched url, redirect to the home state at /
  $urlRouterProvider.otherwise("/");
  //
  // Now set up the states
  $stateProvider
    .state('home', {
      url: "/",
      controller: 'CarouselDemoCtrl as carousel',
      templateUrl: "partials/home.html"
    })
    .state('state1', {
      url: "/state1",
      controller: function($scope) {
        $scope.whatever = "People, this is a test";
      },
      templateUrl: "partials/state1.html"
    })
    .state('state1.list', {
      url: "/list",
      templateUrl: "partials/state1.list.html",
      controller: function($scope) {
        $scope.items = ["A", "List", "Of", "Items"];
      }
    })
    .state('state2', {
      url: "/state2",
      controller: function() {
        this.whatever = "People, this is a tosti";
      },
      controllerAs: 'test',
      templateUrl: "partials/state2.html"
    })
    .state('state2.list', {
      url: "/list",
      templateUrl: "partials/state2.list.html",
      controller: function($scope) {
        $scope.things = ["A", "Set", "Of", "Things"];
      }
    });
});