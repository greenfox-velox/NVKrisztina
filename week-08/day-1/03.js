'use strict';

function Rectangle(a, b){
  this.a = a;
  this.b = b;
}

Rectangle.prototype.getArea = function(){
  return this.a * this.b
}

Rectangle.prototype.getCircumference = function(){
  return 2*this.a + 2*this.b
}

var rectangle1 = new Rectangle(10, 5);
var rectangle2 = new Rectangle(4, 2);
//console.log(rectangle1.getArea());

module.exports.Rectangle=Rectangle;
// Create a constructor for creating Rectangles, it should take two parameters
// as the sides of the rectangle
// Every rectangle should have a method called getArea() that returns its area
// Every rectangle should have a method called getCircumference() that returns its circumference
