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

// var connection = mysql.createConnection({
//   host: 'localhost',
//   user: 'root',
//   password: 'kiwitorta9',
//   database: 'todos'
// });
//
// connection.connect();

//*********************select with express**********************

// app.get('/todos', function(req, res){
//   connection.query('select * from todos', function(err, result){
//     console.log(result);
//     res.send(result);
//   })
// });

app.get('/todos', function(req, res){
    res.send(todo_list);
});

//*********************

function getId (req){
  return todo_list.filter(function (item){
      return item.id === Number(req.params.id)
  });
}

app.get('/todos/:id', function(req, res){
  var filtered = getId(req);
  if (_this.filtered.length === 0) {
    res.sendStatus(404);
  } else {
    res.send(todo_list[req.params.id]);
  }
})

var id_number = todo_list.length;
app.post('/todos', function(req, res){
  req.body["id"] = id_number + 1;
  req.body["completed"] = false;
  todo_list.push(req.body);
  res.send(req.body);
});

app.put('/todos/:id', function(req, res){
  var needed_obj = getId(req);
  console.log(needed_obj);
  if (needed_obj.length !== 0) {
    needed_obj[0]["text"] = req.body.text;
    needed_obj[0]["completed"] = req.body.completed;
    res.send(needed_obj[0]);
  } else {
    req.body["id"] = id_number + 1;
    req.body["completed"] = false;
    todo_list.push(req.body);
    res.send(req.body);
  };
})

app.delete('/todos/:id', function(req, res, next){
 var newtodo = todo_list.filter(function (item){
     return item.id !== Number(req.params.id)
 });
 var filtered = getId(req);
 if (filtered.length === 0) {
   res.sendStatus(404);
 } else {
   filtered[0]["destroyed"] = true;
   res.send(filtered);
   todo_list = newtodo;
 }
});


app.listen(3000);
