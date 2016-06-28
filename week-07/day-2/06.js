'use strict';


// create a function that takes a string and a letter and returns a boolean
// it should return true if the string consits the given letter, false otherwise


function giveBoolean(stringInput, letter){

  var a = stringInput.split('');
  var b = a.some(function(e) {
      return e == letter;
    });
    return b;
};

console.log(giveBoolean('blabla', 'b'))
