var fs = require('fs');

fs.readFile('1.txt', 'utf8', function(err, data){
  fs.writeFile('2.txt', data);
});
