'use strict';

var xhr = new XMLHttpRequest();

xhr.onload = function() {
  var objectRetrieved = JSON.parse(xhr.response);
  objectRetrieved.forEach(function(item, index){
    var newListItem = document.createElement('li');
    var mainListUl = document.querySelector('ul');
    var mainListLabel = document.createElement('label');
    var mainListLabel = document.createElement('img');
    var mainListInput = document.createElement('input');
    mainListUl.appendChild(newListItem);
    newListItem.appendChild(mainListLabel);
    mainListLabel.appendChild(mainListInput);
    newListItem.innerHTML = JSON.parse(xhr.response)[index].text;
    mainListInput.setAttribute('type', 'checkbox');
    mainListInput.setAttribute('class', 'rounded_checkbox');
    mainListInput.setAttribute('name', 'action');
    mainListInput.setAttribute('value', 'JSON.parse(xhr.response)[index].text');
    mainListLabel.setAttribute('src', 'kuka.png');
  });
};

xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos');
xhr.send();
