'use strict';

/*var string2 = 'apple'*/

function countLetters2(string2){
    return string2.split('').reduce(function(acc, index){
    acc[index] = (acc[index] + 1) || 1;
    return acc;
  },{});
};

/*console.log(countLetters2('apple'));*/


module.exports.countLetters2 = countLetters2;
