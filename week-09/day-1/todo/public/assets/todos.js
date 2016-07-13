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
    if (item.completed){
      mainListImage2.setAttribute('src', 'tick.png');
    } else {
      mainListImage2.setAttribute('src', 'circle.png');
    }
    mainListImage2.setAttribute('type', 'checkbox');
    mainListImage2.setAttribute('class', 'rounded_checkbox');
    mainListImage2.addEventListener('click', check);
    mainListImage.setAttribute('src', 'kuka.png');
    mainListImage.addEventListener('click', remove);
    newListItem.setAttribute('data-identifier-forremove', item.id);
    mainListImage.setAttribute('data-identifier-forremove_image', item.id);
    mainListImage2.setAttribute('data-identifier', item.id);
    mainListImage2.setAttribute('data-text', item.text);
    mainListLabel.innerHTML = item.text;
  });
};

xhr.open('GET', 'http://localhost:3000/todos');
xhr.send();


var add_button = document.querySelector('button');
add_button.addEventListener('click', add_item)

function add_item(){
  var xhr2 = new XMLHttpRequest();
  var inputText = document.querySelector('.add_text');
  inputText = JSON.stringify({'text' : inputText.value})
  xhr2.onreadystatechange = function() {
    if(xhr2.readyState == 4 && xhr2.status >= 200) {
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
        newListItem.setAttribute('data-identifier-forremove', JSON.parse(xhr2.responseText).id);
        mainListImage.setAttribute('data-identifier-forremove_image', JSON.parse(xhr2.responseText).id);
        mainListImage2.setAttribute('data-identifier', JSON.parse(xhr2.responseText).id);
        mainListImage2.setAttribute('data-text', JSON.parse(xhr2.responseText).text);
        mainListLabel.innerHTML = JSON.parse(xhr2.responseText).text;
    }
  }

  xhr2.open('POST', 'http://localhost:3000/todos', true);
  xhr2.setRequestHeader("content-type", "application/json; charset=utf-8");
  xhr2.send(inputText);
}

function check(event){
  var xhr3 = new XMLHttpRequest();
  var id = event.target.getAttribute("data-identifier");
  var text = event.target.getAttribute("data-text");
  var text_completed = JSON.stringify({'text' : text, 'completed' : 'true'})
  xhr3.onreadystatechange = function() {
    console.log(xhr3.readyState);
    console.log(xhr3.status);
    if(xhr3.readyState == 4 && xhr3.status >= 200) {
        var addticktome = document.querySelector('[data-identifier="' + JSON.parse(xhr3.response).id + '"]')
        console.log(xhr3.response);
        console.log('[data-identifier="' + JSON.parse(xhr3.response).id + '"]');
        addticktome.setAttribute('src', 'tick.PNG');
  }
  }

  xhr3.open('PUT', 'http://localhost:3000/todos' + '/' + id);
  xhr3.setRequestHeader("content-type", "application/json; charset=utf-8");
  xhr3.send(text_completed);
}

function remove(event){
  var xhr4 = new XMLHttpRequest();
  var id = event.target.getAttribute("data-identifier-forremove_image");
  xhr4.onreadystatechange = function() {
    if(xhr4.readyState == 4 && xhr4.status >= 200) {
        var mainListUl = document.querySelector('ul');
        var removable = document.querySelector('[data-identifier-forremove="' + JSON.parse(xhr4.response)[0].id + '"]')
        console.log('[data-identifier-forremove="' + JSON.parse(xhr4.response)[0].id + '"]');
        console.log(xhr4.response);
        console.log(JSON.parse(xhr4.response)[0].id);
        mainListUl.removeChild(removable);
  }
  }

  xhr4.open('DELETE', 'http://localhost:3000/todos' + '/' + id);
  xhr4.setRequestHeader("content-type", "application/json; charset=utf-8");
  xhr4.send();
}
