'use strict'

var numbers = [4, 5, 2, 15, 9];

numbers.forEach(function(e, i, arr){

});

/*adott elem, adott index az egész numbers tömb*/

var sum = numbers.reduce(function(acc, e, i, arr){
  return acc + e;
}, 0);

/*console.log(sum);*/
/*akkumulátor = zseb, adott elem, adott index az egész numbers tömb*/

var evens = numbers.reduce(function(acc, e){
  if (e % 2 === 0) {
    acc.push(e);
  }
  return acc;
}, []);

console.log(evens);
