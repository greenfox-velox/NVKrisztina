'use strict';

var y = 'seasons';
var out = 6;
// if the last and the first letter of the string
// are the same double the variable
// called out, if not half it

var l = 0;
l = y.length;

if (y[0] === y[l - 1]){

  out = out * 2;

}else {

  out = out / 2;

};

console.log(out);
