'use strict'

var paragraphs = document.querySelectorAll('p');
paragraphs.forEach(function(item, index){
  if (item.classList.contains("cat")){
    alert('Yeah cat!')
  }
});

var apple = document.querySelector('p');

paragraphs.forEach(function(item, index){
  if (item.classList.contains("dolphin")){
    apple.textContent = 'pear';
  }
});

var cat = document.querySelectorAll('p')[2];

paragraphs.forEach(function(item, index){
  if (item.classList.contains("apple")){
    cat.textContent = 'dog';
  }
});

apple.setAttribute("background-color", "red");

var balloon = document.querySelector('.balloon');
balloon.classList.remove('balloon');
