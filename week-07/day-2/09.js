'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 2, p: 2, l: 1}

function countLetters(string){

var b = {};
var a = string.split('');
a.forEach(function(e){
  if (e in b){
  b[e] += 1;
} else {
  b[e] = 1;
}
  });

console.log(b);
}
countLetters('apple');

//a.filter(function(e){
  //return 1;
