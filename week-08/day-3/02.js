'use strict';

var fs = require('fs');

// create a function takes three parameters:
//  - fileName: the name of the file
//  - letter: a character
//  - cb: callback (with two parameters: error and the result)
//
// it should read the file and count the letters in the content
// and it should call the callback with the counted number
// if there is some error it should call the callback with the error
//

function countLetters(fileName, letter, cb){
  var summa = 0;
  fs.readFile(fileName, function(err, content){
    if (err){
      return cb(err);
    }
    var lengthNumber = String(content).split('').forEach(function(item, index){
      if (item == letter){
        summa += 1;
      }
    });
    cb(null, summa);
  });
}

countLetters('1.txt', 'a', function(err, c){
  console.log(err, c);
})
