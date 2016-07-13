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
    console.log(result);
    res.send(result);
  })
});

//*************************************************************

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

//*******************post*(insert)*****************************************

app.post('/todos', function(req, res){
  connection.query('insert into todos set ?', req.body, function(err, reso){
    console.log(result.id);
    if(err){
      console.error(err);
      return;
    }
    console.error(result);
    //console.log(result);
    reso = {};
    reso.id = 0;
    reso.text = req.body.text;
    reso.completed = "false";
    console.log(reso);
    res.send(reso);
  });
});


//********************put*(update)****************************************

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


//*****************************delete*****************************************

app.delete('/todos/:id', function(req, res){
  connection.query('DELETE FROM todos WHERE id = ?', req.id, function (err, result) {
      if (err) throw err;
      console.log('Deleted ' + result.affectedRows + ' rows');
      res.send(result);
  })
});


app.listen(3000);
