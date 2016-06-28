'use strict';

// Create a function that takes a number and returns it as string in English
// like 0 -> "zero", it should work with the first 5 numbers, after it should
// return "many"

function returnasString(number){

switch (number) {
  case 0:
    console.log('zero');
    break;
  case 1:
    console.log('one');
    break;
  case 2:
    console.log('two');
    break;
  default:
    console.log('many');
    break;
};
};
returnasString(2);
