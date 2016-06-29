'use strict'

var image = document.querySelector('img');
console.log(image.getAttribute("src"));

image.setAttribute("src", "http://www.vetprofessionals.com/catprofessional/images/home-cat.jpg");

var link = document.querySelector('a');
link.setAttribute("href", "http://www.greenfoxacademy.com/");

var button = document.querySelector('.this-one').disabled = true;
document.querySelector('.this-one').textContent = "Don't click me";
