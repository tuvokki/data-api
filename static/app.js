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

myApp.component('gridshow', {
  bindings: {
    slides: '='
  },
  controller: function($scope) {
    var self = this;
    this.rows = [];
    console.log('test', this);

    $scope.$watch(angular.bind(this, function () { 
        if (this.slides) {
          this.rows = [];
          var tmpObject = [];
          var counter = 1;
          for (var i = 0; i < this.slides.length; i++) {
            tmpObject.push(this.slides[i].image);
            if (counter++ == 4){
              self.rows.push({
                title: 'Row ' + this.rows.length,
                images: tmpObject
              });
              counter = 1;
              tmpObject = [];
            }
          };
          self.rows.push({
                title: 'Row ' + this.rows.length,
                images: tmpObject
              });
        }
        return this.slides;
    }), function(value) {
        console.log('Name change to ' + value);
    });
  },
  controllerAs: 'grid',
  templateUrl: 'partials/showgrid.html'
});

myApp.component('counter', {
  bindings: {
    count: '='
  },
  controller: function () {
    function increment() {
      this.count++;
    }
    function decrement() {
      this.count--;
    }
    this.increment = increment;
    this.decrement = decrement;
  },
  controllerAs: 'klapsigaar',
  template: function ($element, $attrs) {
    // access to $element and $attrs
    return [
      '<div class="todo">',
        '<input type="text" ng-model="klapsigaar.count">',
        '<button type="button" ng-click="klapsigaar.decrement();">-</button>',
        '<button type="button" ng-click="klapsigaar.increment();">+</button>',
      '</div>'
    ].join('')
  }
});

myApp.controller('CarouselDemoCtrl', function($log, Slides) {
  var self = this;
  this.myInterval = 0; //disable autoscrolling
  this.noWrapSlides = true; //stop at the last slide
  
  Slides.getSlides().then(function(slides) {
    //$log.debug(slides.data.slides);
    self.slides = slides.data.slides;
  }, function errorCallback(response) {
    $log.error('no slides: ', response)
  });
});

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
    .state('examples', {
      url: "/examples",
      controller: function($log, Slides) {
        var self = this;
        self.count = 8;
        self.whatever = "People, this is a test " + self.count;
        Slides.getSlides().then(function(slides) {
            //$log.debug(slides.data.slides);
            self.slidelist = slides.data.slides;
          }, function errorCallback(response) {
            $log.error('no slides: ', response)
          });
      },
      controllerAs: 'examples',
      templateUrl: "partials/examples.html"
    // })
    // .state('examples.list', {
    //   url: "/list",
    //   templateUrl: "partials/examples.list.html",
    //   controller: function($scope) {
    //     $scope.items = ["A", "List", "Of", "Items"];
    //   }
    // })
    // .state('state2', {
    //   url: "/state2",
    //   controller: function() {
    //     this.whatever = "People, this is a tosti";
    //   },
    //   controllerAs: 'test',
    //   templateUrl: "partials/state2.html"
    // })
    // .state('state2.list', {
    //   url: "/list",
    //   templateUrl: "partials/state2.list.html",
    //   controller: function($scope) {
    //     $scope.things = ["A", "Set", "Of", "Things"];
    //   }
    });
});