'use strict';

var button = document.querySelector('button');
button.addEventListener('click', sendData)



function sendData(data){
  var xhr = new XMLHttpRequest();
  var inputText = document.querySelector('#sentence');
  xhr.onload = function() {
    alert(xhr.response);
  };

  xhr.open('GET', 'https://yoda.p.mashape.com/yoda?sentence=' + inputText.value.split(' ').join('+'));
  xhr.setRequestHeader("X-Mashape-Key", "p7unPZtBDfmshtBEvZXqD2rsFMcJp179X3hjsnx5kgixMTQiAp");
  xhr.send();
}
