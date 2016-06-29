'use strict'

var one = document.querySelector('.output1');

var firstParagraph = document.querySelector('p');

one.textContent = firstParagraph.textContent;
console.log(one.textContent);

var two = document.querySelector('.output2');
two.innerHTML = firstParagraph.innerHTML;
console.log(two.innerHTML);
