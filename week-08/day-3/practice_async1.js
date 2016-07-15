'use strict';

var fs = require('fs')

function writeFiletoConsole (filename, cb){
  fs.readFile(filename, function(err, content){
    if (err){
      return cb(err)
    }
    cb(null, String(content))
  })
}

writeFiletoConsole('1.txt', function(err, content){
  console.log(err, content);
})
