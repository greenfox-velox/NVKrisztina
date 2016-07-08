'use strict';

var xhr = new XMLHttpRequest();

xhr.onload = function() {
  var objectRetrieved = JSON.parse(xhr.response);
  objectRetrieved.forEach(function(item, index){
    var newListItem = document.createElement('li');
    var mainListUl = document.querySelector('ul');
    var mainListLabel = document.createElement('label');
    var mainListImage = document.createElement('img');
    var mainListInput = document.createElement('input');
    mainListUl.appendChild(newListItem);
    newListItem.appendChild(mainListLabel);
    newListItem.appendChild(mainListImage);
    newListItem.appendChild(mainListInput);
    mainListInput.setAttribute('type', 'checkbox');
    mainListImage.setAttribute('src', 'kuka.png');
    mainListLabel.innerHTML = JSON.parse(xhr.response)[index].text;
  });
};

xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos');
xhr.send();


var add_button = document.querySelector('button');
add_button.addEventListener('click', add_button_works)

function add_button_works(){
  var xhr2 = new XMLHttpRequest();
  var inputText = document.querySelector('.add_text');
  inputText = JSON.stringify({'text' : inputText.value})
  xhr2.onreadystatechange = function() {
    if(xhr2.readyState == 4 && xhr2.status >= 200) {
        alert(xhr2.responseText);
        var text = JSON.parse(xhr2.responseText).text;
    //  var id = JSON.parse(xhr2.responseText).id;
        var newListItem = document.createElement('li');
        var mainListUl = document.querySelector('ul');
        var mainListLabel = document.createElement('label');
        var mainListImage = document.createElement('img');
        var mainListInput = document.createElement('input');
        mainListUl.insertBefore(newListItem, newListItem[0]);
        newListItem.appendChild(mainListLabel);
        newListItem.appendChild(mainListImage);
        newListItem.appendChild(mainListInput);
        mainListInput.setAttribute('type', 'checkbox');
        mainListInput.setAttribute('class', 'rounded_checkbox');
        mainListInput.setAttribute('name', 'action');
        mainListImage.setAttribute('src', 'kuka.png');
        mainListLabel.innerHTML = text;
    }
  }

  xhr2.open('POST', 'https://mysterious-dusk-8248.herokuapp.com/todos', true);
  xhr2.setRequestHeader("content-type", "application/json; charset=utf-8");
  xhr2.send(inputText);
}
