'use strict';

var fs = require('fs');

function wordCount(filename, cb) {
  fs.readFile(filename, function(err, content){
    if (err){
      return cb(err);
    }
    cb(null, String(content).split(/\s/g).length);
  });

}

wordCount('1.txt', function(err, c){
  console.log(err, c);
})










//1:
[1, 2, 3].forEach(log);

function log(e) {
  console.log(e);
}


//1.uaz:
[].foreEach(function(e){
  console.log(e)
})
