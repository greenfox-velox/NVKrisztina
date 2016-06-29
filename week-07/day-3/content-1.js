'use strict'

var heading = document.querySelector('h1');
alert(heading);

var paragraph = document.querySelector('p');
console.log(paragraph);

var paragraph2 = document.querySelectorAll('p')[1];
alert(paragraph2);

heading.textContent = 'New content'
console.log(heading.textContent);

var lastParagraph = document.querySelectorAll('p')[2];
lastParagraph.textContent = paragraph.textContent;
console.log(lastParagraph.textContent);
