'use strict';

var xhr = new XMLHttpRequest();

xhr.onload = function() {
  var objectRetrieved = JSON.parse(xhr.response);
  objectRetrieved.forEach(function(item, index){
    var newListItem = document.createElement('li');
    var mainListUl = document.querySelector('ul');
    var mainListLabel = document.createElement('label');
    var mainListImage = document.createElement('img');
    var mainListImage2 = document.createElement('img');
    mainListUl.appendChild(newListItem);
    newListItem.appendChild(mainListLabel);
    newListItem.appendChild(mainListImage);
    newListItem.appendChild(mainListImage2);
    mainListImage2.setAttribute('src', 'circle.png');
    mainListImage2.setAttribute('type', 'checkbox');
    mainListImage2.setAttribute('class', 'rounded_checkbox');
    mainListImage2.addEventListener('click', check);
    mainListImage.setAttribute('src', 'kuka.png');
    mainListImage.addEventListener('click', remove);
    mainListImage.setAttribute('data-identifier-forRemove', item.id);
    mainListImage2.setAttribute('data-identifier', item.id);
    mainListImage2.setAttribute('data-text', item.text);
    mainListLabel.innerHTML = item.text;
  });
};

xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos');
xhr.send();


var add_button = document.querySelector('button');
add_button.addEventListener('click', add_item)

function add_item(){
  var xhr2 = new XMLHttpRequest();
  var inputText = document.querySelector('.add_text');
  inputText = JSON.stringify({'text' : inputText.value})
  xhr2.onreadystatechange = function() {
    if(xhr2.readyState == 4 && xhr2.status >= 200) {
        alert(xhr2.responseText);
        var text = JSON.parse(xhr2.responseText).text;
        var newListItem = document.createElement('li');
        var mainListUl = document.querySelector('ul');
        var mainListLabel = document.createElement('label');
        var mainListImage = document.createElement('img');
        var mainListImage2 = document.createElement('img');
        mainListUl.insertBefore(newListItem, newListItem[0]);
        newListItem.appendChild(mainListLabel);
        newListItem.appendChild(mainListImage);
        newListItem.appendChild(mainListImage2);
        mainListImage2.setAttribute('src', 'circle.png');
        mainListImage2.setAttribute('type', 'checkbox');
        mainListImage2.setAttribute('class', 'rounded_checkbox');
        mainListImage2.addEventListener('click', check);
        mainListImage.setAttribute('src', 'kuka.png');
        mainListImage.addEventListener('click', remove);
        mainListImage.setAttribute('data-identifier-forRemove', JSON.parse(xhr2.responseText).id);
        mainListImage2.setAttribute('data-identifier', JSON.parse(xhr2.responseText).id);
        mainListImage2.setAttribute('data-text', JSON.parse(xhr2.responseText).text);
        mainListLabel.innerHTML = JSON.parse(xhr2.responseText).text;
    }
  }

  xhr2.open('POST', 'https://mysterious-dusk-8248.herokuapp.com/todos', true);
  xhr2.setRequestHeader("content-type", "application/json; charset=utf-8");
  xhr2.send(inputText);
}

function check(event){
  var xhr3 = new XMLHttpRequest();
  var id = event.target.getAttribute("data-identifier");
  var text = event.target.getAttribute("data-text");
  var text_completed = JSON.stringify({'text' : text, 'completed' : 'true'})
  xhr3.onreadystatechange = function() {
    if(xhr3.readyState == 4 && xhr3.status >= 200) {
        alert(xhr3.response);
  }
  }

  xhr3.open('PUT', 'https://mysterious-dusk-8248.herokuapp.com/todos' + '/' + id);
  xhr3.setRequestHeader("content-type", "application/json; charset=utf-8");
  xhr3.send(text_completed);
}

function remove(event){
  var xhr4 = new XMLHttpRequest();
  var id = event.target.getAttribute("data-identifier-forRemove");
  xhr4.onreadystatechange = function() {
    if(xhr4.readyState == 4 && xhr4.status >= 200) {
        alert(xhr4.response);
        var text = JSON.parse(xhr4.responseText).text;
        var newListItem = document.createElement('li');
        var mainListUl = document.querySelector('ul');
        var mainListLabel = document.createElement('label');
        var mainListImage = document.createElement('img');
        var mainListImage2 = document.createElement('img');
        mainListUl.insertBefore(newListItem, newListItem[0]);
        newListItem.appendChild(mainListLabel);
        newListItem.appendChild(mainListImage);
        newListItem.appendChild(mainListImage2);
        mainListImage2.setAttribute('src', 'circle.png');
        mainListImage2.setAttribute('type', 'checkbox');
        mainListImage2.setAttribute('class', 'rounded_checkbox');
        mainListImage2.addEventListener('click', check);
        mainListImage.setAttribute('src', 'kuka.png');
        mainListImage.addEventListener('click', remove);
        mainListImage.setAttribute('data-identifier-forRemove', JSON.parse(xhr4.responseText).id);
        mainListImage2.setAttribute('data-identifier', JSON.parse(xhr4.responseText).id);
        mainListImage2.setAttribute('data-text', JSON.parse(xhr4.responseText).text);
        mainListLabel.innerHTML = JSON.parse(xhr4.responseText).text;
  }
  }

  xhr4.open('DELETE', 'https://mysterious-dusk-8248.herokuapp.com/todos' + '/' + id);
  xhr4.setRequestHeader("content-type", "application/json; charset=utf-8");
  xhr4.send();
}
