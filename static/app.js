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
    rows: '='
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

myApp.component('navigation', {
  templateUrl: 'partials/navigation.html'
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

myApp.controller('ModalInstanceCtrl', function ($uibModalInstance, items) {
  var self = this;

  self.items = items;
  self.selected = {
    item: self.items[0]
  };

  self.ok = function () {
    $uibModalInstance.close(self.selected.item);
  };

  self.cancel = function () {
    $uibModalInstance.dismiss('cancel');
  };
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

        Slides.getSlides().then(function(slides) {
          var slidelist = slides.data.slides;

          self.rows = [];
          var tmpObject = [];
          var counter = 1;
          for (var i = 0; i < slidelist.length; i++) {
            tmpObject.push(slidelist[i].image);
            if (counter++ == 4){
              self.rows.push({
                title: 'Row ' + self.rows.length,
                images: tmpObject
              });
              counter = 1;
              tmpObject = [];
            }
          };
          self.rows.push({
            title: 'Row ' + self.rows.length,
            images: tmpObject
          });
        }, function errorCallback(response) {
          $log.error('no slides: ', response)
        });
      },
      controllerAs: 'examples',
      templateUrl: "partials/examples.html"
    })
    // .state('examples.list', {
    //   url: "/list",
    //   templateUrl: "partials/examples.list.html",
    //   controller: function($scope) {
    //     $scope.items = ["A", "List", "Of", "Items"];
    //   }
    // })
    .state('modalz', {
      url: "/modalz",
      controller: function($uibModal, $log) {
        var self = this;
        this.whatever = "People, this is a " + this.selected + " tosti";
        this.items = ['item1', 'item2', 'item3'];
        self.openmdl = function openmdl(size) {

          var modalInstance = $uibModal.open({
            animation: true,
            templateUrl: 'partials/modal.html',
            controller: 'ModalInstanceCtrl',
            controllerAs: 'modal',
            size: size,
            resolve: {
              items: function () {
                return ['item1', 'item2', 'item3'];
              }
            }
          });

          modalInstance.result.then(function (selectedItem) {
            $log.debug('returned ', selectedItem);
            self.selected = selectedItem;
          }, function () {
            $log.info('Modal dismissed at: ' + new Date());
          });
        };
      },
      controllerAs: 'test',
      templateUrl: "partials/modalz.html"
    // })
    // .state('state2.list', {
    //   url: "/list",
    //   templateUrl: "partials/state2.list.html",
    //   controller: function($scope) {
    //     $scope.things = ["A", "Set", "Of", "Things"];
    //   }
    });
});