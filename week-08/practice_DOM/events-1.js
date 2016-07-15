'use strict';

var button = document.querySelector('button');
button.addEventListener('click', displayDate);

function displayDate(event) {
    document.querySelector('p').textContent = Date();
    alert(event.target.nodeName);
}

//The target event property returns the element that triggered
//the event.
