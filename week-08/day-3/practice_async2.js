'use strict';

var fs = require('fs');

function writetoAnotherFile(filename1, filename2, cb){
  fs.readFile(filename1, function(err, content){
    if (err){
      return cb(err)
    }
    fs.writeFile(filename2, String(content), function(err){
      if (err){
        return cb(err)
      }
      cb(null);
    });
  })
}

writetoAnotherFile('1.txt', '2.txt', function(err, content){
  console.log(err);
});
