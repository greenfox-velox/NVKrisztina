//the entire practice_project is the Net Ninja
//YoutTube tutorial material, not my own work

var express = require('express');
var todoController = require('./controllers/todoController');

var app = express();

app.set('view engine', 'ejs');

app.use(express.static('./public'))

app.listen(3000);

todoController(app);
