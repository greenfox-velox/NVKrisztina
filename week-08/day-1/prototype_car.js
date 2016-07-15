'use strict';

function Car(km){
  this.km = km;
}
/*a metódusokat a prototype-on definiáljuk, nem fönt*/
Car.prototype.ride = function(km){
  this.km += km;
}

var opel = new Car(40000);

opel.ride(120);
