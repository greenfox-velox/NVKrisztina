'use strict';

var numbers = [2, 5, 11, 29];

// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise

var numbers = [2, 5, 11, 29].every(function(e){

});

console.log(numbers);

function isaPrime(number){
  var i = 2
  while((i <= number) && (number % i !== 0)){
    i ++
    if (i === number){
      return true
    }
    }
  return false
  }
​
​
function primeinarray(listofnum){
  return listofnum.map(isaPrime)
}
​
​
console.log(isaPrime(21));
console.log(primeinarray(numbers));
//var a = Math.random() * 10;
  //return e / a !== 0;
//  console.log(e);
