'use strict'

var parent = document.querySelector('ul');
var child = document.querySelector('li');

var removed = parent.removeChild(child);

var l = ['apple', 'bubble', 'cat', 'green fox'];
console.log(parent);

l.forEach(function(item, index){
  var newLiii = document.createElement('li');
  newLiii.textContent = item;
  parent.appendChild(newLiii);
});
