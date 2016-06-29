'use strict'

var newLi = document.createElement("li");
var newLi2 = document.createElement("li");

var uls = document.querySelector('ul');
uls.appendChild(newLi);
newLi.innerHTML = "The Green Fox";
uls.appendChild(newLi2);
newLi2.innerHTML = "The Lamplighter";

var newHeading = document.createElement("h1");
var container = document.querySelector('.container');
container.appendChild(newHeading);
newHeading.innerHTML = "I can add elements to the DOM!";

var image = document.createElement("img");
container.appendChild(image);
image.src = "https://pixabay.com/static/uploads/photo/2014/03/29/09/17/cat-300572_960_720.jpg";
