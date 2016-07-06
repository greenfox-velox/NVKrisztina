'use strict';

var fs = require('fs');
// Create a function that takes 3 parameters
//  - file1: a filename
//  - file2: a filename
//  - cb: callback (with two paramteres: error and contents)
//
// It should read both files and concat their content
// then it should call the callback with the concated contents
// if any error occures it should call the callback with an error

function concatContent(filename, filename2, cb){
  fs.readFile(filename, function(err, content){
    if (err){
      return cb(err);
    }
    fs.readFile(filename2, function(err, content2){
      if (err){
        return cb(err);
      }
      cb(null, String(content) + String(content2));
});
});
}
concatContent('1.txt', '2.txt', function(err, content){
  console.log(err, content);
});
