'use strict';

var fs = require('fs');
// create a function that takes 3 parameters
//  - readFileName: a filename where it reads from
//  - wirteFileName: a filename where it writes to
//  - cb: callback with one parameter: the error if occured
//
// It should read the file named readFileName and double the text of the file
// like: "apple" -> "appleapple"
// Than it should write this doubled text to the file named writeFileName
// When it finished it should call the callback with a null
// If there is any error during the process it should call the callback with the error

function doubleFileText(readFileName, writeFileName, cb){
  fs.readFile(readFileName, function(err, content){
    if (err){
      return cb(err);
    }
    fs.writeFile(writeFileName, String(content) + String(content), function(err, content){
      if (err){
        return cb(err);
      }
    });
    cb(null);
  });

  }

doubleFileText('1.txt', '2.txt', function(err){
  console.log(err);
});
