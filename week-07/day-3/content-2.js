'use strict'

var paragraphLast = document.querySelector('.dog');
paragraphLast.textContent

var allPs = document.querySelectorAll('p');
console.log(allPs);

allPs.forEach(function(item, index){
    item.textContent = paragraphLast.textContent;
    //console.log(item.textContent)
});
