'use strict';


var button = document.querySelector('button');
button.addEventListener('click', getRequest)

function getRequest(){
  var xhr = new XMLHttpRequest();
  xhr.onload = function() {
    var celebrations = JSON.parse(xhr.response).celebrations.length;
    var date = JSON.parse(xhr.response).date;
    alert('Celebrations: ' + celebrations + ' Date: ' + date);
  };
  xhr.open('GET', 'http://calapi.inadiutorium.cz/api/v0/en/calendars/default/2016/7/6')
  xhr.send();
}
