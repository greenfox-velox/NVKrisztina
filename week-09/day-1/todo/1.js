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

var newItem = {
    "completed": false,
    "id": 4,
    "text": "Water the plants"
}

var express = require('express');
var bodyParser = require('body-parser');
var app = express();
app.use(bodyParser.urlencoded());
app.use(bodyParser.json());


app.get('/todos', function(req, res){
  res.send(todo_list);
});

app.get('/todos/:id', function(req, res){
  res.send(todo_list[req.params.id]);
});

var id_number = todo_list.length;
app.post('/todos', function(req, res){
  //console.log(JSON.stringify(req.body));
  req.body["id"] = id_number + 1;
  req.body["completed"] = false;
  todo_list.push(req.body);
});

app.put('/todos/:id', function(req, res){
  var needed_obj = todo_list.filter(function(item){
    return item.id === Number(req.params.id);
  })
  if (needed_obj.length !== 0) {
    needed_obj[0]["text"] = req.body.text;
    needed_obj[0]["completed"] = req.body.completed;
  } else {
    req.body["id"] = id_number + 1;
    req.body["completed"] = false;
    todo_list.push(req.body);
  };
})

app.delete('/todos/:id', function(req, res){
 var newtodo = todo_list.filter(function (item){
     return item.id !== Number(req.params.id)
 });
 var filtered = todo_list.filter(function (item){
     return item.id === Number(req.params.id)
 });
 filtered[0]["destroyed"] = true;
 res.json(filtered);
 todo_list = newtodo;
});

app.listen(3000);
