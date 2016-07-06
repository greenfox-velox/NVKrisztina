'use strict';

// create a function that takes a filename reads the content of the file
// and counts the words in it. It should not return the result, rather
// call a callback (its second parameter)
// The callback should have two parameters:
//  - err: the error object if anything wrong happened
//  - count: the word count
//Mate megoldasa

var fs = require('fs');

countWordsinaFile(filename, callback){
      fs.readFile(filename, function(err, data){
      var count = String(data).split(" ").length;
      callback(err, count);
  });
});

function writeOut(err, count){
  console.log(count);
}

countWordsinaFile('1.txt', writeOut)
