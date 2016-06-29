'use strict'

var parent = document.querySelector('ul');
var child = document.querySelector('li');

var removed = parent.removeChild(child);

var newChild1 = document.createElement('li');
var newChild2 = document.createElement('li');
var newChild3 = document.createElement('li');

parent.appendChild(newChild1);
parent.appendChild(newChild2);
parent.appendChild(newChild3);

newChild1.textContent = "The Fox";
newChild2.textContent = "The Fox";
newChild3.textContent = "The Fox";
