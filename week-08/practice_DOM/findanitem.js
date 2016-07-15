'use strict';

//fajtája(pl div, button, ul, p, h1 stb pont nélkül)
var add_button = document.querySelector('button');
console.log(add_button);

//class neve
var x = document.querySelectorAll('.add_button');
console.log(x);

//2 class is van
var y = document.querySelector('.add_button.b45')
console.log(y);

//ha 2 különb elemet keresek, köztük vessző
var conceitedKing = document.querySelectorAll('#b325, .asteroid.b326');

// 2. p
var paragraph2 = document.querySelectorAll('p')[1];

//textContent
var heading = document.querySelector('h1');
heading.textContent = 'my love'

//innerHTML
var z = document.querySelectorAll('label')[2];
console.log(z.innerHTML);
console.log(z.textContent);

//**********************************************************
// Write the image's url to the console.
//<img src="https://static.wixstatic.c ...
var image = document.querySelector('img');
//console.log(image.getAttribute("src"));

//Set it to another image
//image.setAttribute("src", "http://www.vetprofe...")

//**********************************************************
//The classList property returns the class name(s)
//of an element, as a DOMTokenList object.
var labels = document.querySelector('button')
console.log(labels.classList);
//["add_button", value: "add_button"]
labels.classList.add('new');
console.log(labels.classList);
//
//if (item.classList.contains("cat")){
//  alert('Yeah cat!')
//}
//
//balloon.classList.remove('balloon');
//
labels.classList.toggle('old');
console.log(labels.classList);

labels.classList.toggle('old');
console.log(labels.classList);
