'use strict';

//function loadItemWhenPageOpen(){
var xhr = new XMLHttpRequest();

//function createItems(){


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
    mainListInput.setAttribute('id', 'action');
    mainListInput.setAttribute('name', 'action');
    mainListInput.setAttribute('value', 'JSON.parse(xhr.response)[index].text');
    mainListLabel.setAttribute('src', 'kuka.png');
  });
};

xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos');
xhr.send();

//console.log(JSON.parse(xhr.response)[index].text);




//loadItemWhenPageOpen()
