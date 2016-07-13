var express = require('express');

var app = express();

app.get('/', function(req, res) {
  res.send('This path name: ' + req.url + ', Request method: ' + 'Content-Type: text/plain' + ', Current time: ' + Date());
});

app.listen(3000);
console.log('hey');
