var todo_list = [
    {
        "completed": false,
        "id": 1,
        "text": "Buy milk"
    },
    {
        "completed": false,
        "id": 2,
        "text": "Make dinner"
    },
    {
        "completed": false,
        "id": 3,
        "text": "Save the world"
    }
]

var express = require('express');
var bodyParser = require('body-parser');
var app = express();
app.use(bodyParser.urlencoded());
app.use(bodyParser.json());
app.use(express.static('./public/assets'))

var mysql = require('mysql');

var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'kiwitorta9',
  database: 'todos'
});

connection.connect();

//*********************select with express**********************

app.get('/todos', function(req, res){
  connection.query('select * from todos', function(err, result){
    res.send(result);
  })
});

//*************************************************************

app.get('/todos/:id', function(req, res){
  connection.query('select * from todos where id = ?', req.params.id, function(err, result){
  if (err) {
    console.error(err);
    return;
  }
    res.send(result[0]);
  });
});

//*******************post*(insert)******************************

app.post('/todos', function(req, res){
  connection.query('insert into todos set ?', req.body, function(err, result){
    console.log(result.id);
    if(err){
      console.error(err);
      return;
    }
    console.error(result);
    result = {};
    result.id = 0;
    result.text = req.body.text;
    result.completed = "false";
    res.send(result);
  });
});

//********************put*(update)******************************

app.put('/todos/:id', function(req, res){
  connection.query('UPDATE todos SET completed = "true" where id = ?', req.params.id, function(err, result){
    if(err){
      console.error(err);
      return;
    }
    console.error(result);
    result = {};
    result.id = req.params.id;
    result.text = req.body.text;
    result.completed = "true";
    res.send(result);
  });
});


//*****************************delete******************************

app.delete('/todos/:id', function(req, res){
  console.log(req.params.id);
  connection.query('UPDATE todos SET destroyed = "true" Where id = ?', req.params.id, function (err, result) {
      if (err) throw err;
      console.log('Changed ' + result.affectedRows + ' rows');
      res.send(result);
  })
});

// var filtered = getId(req);
// if (filtered.length === 0) {
//   res.sendStatus(404);
// } else {
//   filtered[0]["destroyed"] = true;
//   res.send(filtered);


app.listen(3000);
