'use strict'

var paragraphs = document.querySelectorAll('li');
var l = ['apple', 'banana', 'cat', 'dog'];

paragraphs.forEach(function(item, index){
  item.textContent = l[index];
});
