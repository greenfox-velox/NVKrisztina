'use strict';

// write a function called each that takes an array and a function as a parameter
// and calls the function with each element of the array as parameter
// so it should call the array 3 times if the array has 3 elements

function each(fun, arrayInput){

  var num = 0;
  for (num; num < arrayInput.length; num++){
  fun(arrayInput[num]);
}
}

each(console.log, [1, 2, 3]);
