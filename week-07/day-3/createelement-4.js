'use strict'


var parent = document.querySelector('ul');
var child = document.querySelector('li');

var removed = parent.removeChild(child);

planetData.forEach(function(item, index){

  if (item.asteroid){
    var newLiAgain = document.createElement("li");
    newLiAgain.textContent = item.content;
    parent.appendChild(newLiAgain);
  }
});
