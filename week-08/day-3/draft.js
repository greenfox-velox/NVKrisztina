'use strict';

var fs = require('fs');

fs.readFile('1.txt')

console.log()



function countLetters(fileName, letter, cb){
  fs.readFile(fileName, function(err, content){
    if (err){
      return cb(err);
    }
    var lengthNumber = String(content).length;
    cb(null, lengthNumber);
  });

}

countLetters('1.txt', 'a', function(err, c){
  console.log(err, c);
})
