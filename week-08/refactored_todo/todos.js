'use strict';

var url = 'https://mysterious-dusk-8248.herokuapp.com/todos';

//*****************get************************

function getTodos(giveTodos) {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', url);
  xhr.onload = function() {
    var response = JSON.parse(xhr.response);
    giveTodos(response);
    };
xhr.send();
};

function createMoreElements(response){
  response.forEach(function(response){
    createOneElement(response);
  });
}

getTodos(createMoreElements);

//******************add****************************

var add_button = document.querySelector('button');
add_button.addEventListener('click', addTodo)

function addTodo(){
  var xhr = new XMLHttpRequest();
  var inputText = document.querySelector('.add_text');
  inputText = JSON.stringify({'text' : inputText.value})
  xhr.onload = function() {
    var response = JSON.parse(xhr.response);
    createOneElement(response);
  }
  xhr.open('POST', url, true);
  xhr.setRequestHeader("content-type", "application/json; charset=utf-8");
  xhr.send(inputText);
}

//*******************check***********************

function check(event){
  var xhr = new XMLHttpRequest();
  var id = event.target.getAttribute("data-identifier");
  var text = event.target.getAttribute("data-text");
  var text_completed = JSON.stringify({'text' : text, 'completed' : 'true'})
  xhr.onreadystatechange = function() {
    if(xhr.readyState == 4 && xhr.status >= 200) {
        var addticktome = document.querySelector('[data-identifier="' + JSON.parse(xhr.response).id + '"]')
        addticktome.setAttribute('src', 'tick.PNG');
    }
  }
  xhr.open('PUT', url + '/' + id);
  xhr.setRequestHeader("content-type", "application/json; charset=utf-8");
  xhr.send(text_completed);
}

//********************remove*********************

function remove(event){
  var xhr = new XMLHttpRequest();
  var id = event.target.getAttribute("data-identifier-forremove_image");
  xhr.onreadystatechange = function() {
    if(xhr.readyState == 4 && xhr.status >= 200) {
        var mainListUl = document.querySelector('ul');
        var removable = document.querySelector('[data-identifier-forremove="' + JSON.parse(xhr.response).id + '"]')
        mainListUl.removeChild(removable);
    }
  }
  xhr.open('DELETE', url + '/' + id);
  xhr.setRequestHeader("content-type", "application/json; charset=utf-8");
  xhr.send();
}

//*********************create one element***********

function createOneElement (response){
  var newListItem = document.createElement('li');
  var mainListUl = document.querySelector('ul');
  var mainListLabel = document.createElement('label');
  var mainListImage = document.createElement('img');
  var mainListImage2 = document.createElement('img');
  mainListUl.appendChild(newListItem);
  newListItem.appendChild(mainListLabel);
  newListItem.appendChild(mainListImage);
  newListItem.appendChild(mainListImage2);
  if (response.completed){
    mainListImage2.setAttribute('src', 'tick.png');
  } else {
    mainListImage2.setAttribute('src', 'circle.png');
  }
  mainListImage2.setAttribute('type', 'checkbox');
  mainListImage2.setAttribute('class', 'rounded_checkbox');
  mainListImage2.addEventListener('click', check);
  mainListImage.setAttribute('src', 'kuka.png');
  mainListImage.addEventListener('click', remove);
  newListItem.setAttribute('data-identifier-forremove', response.id);
  mainListImage.setAttribute('data-identifier-forremove_image', response.id);
  mainListImage2.setAttribute('data-identifier', response.id);
  mainListImage2.setAttribute('data-text', response.text);
  mainListLabel.innerHTML = response.text;
};
