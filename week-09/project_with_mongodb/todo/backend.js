var mongodb = require('mongodb');
var MongoClient = mongodb.MongoClient;

var url = 'mongodb://localhost:27017/my_todos';

MongoClient.connect(url, function (err, db) {
  if (err) {
    console.log('Unable to connect to the mongoDB server. Error:', err);
  } else {
    console.log('Connection established to', url);

var collection = db.collection('my_todos');

var id_number = 3;

var todo1 = {"completed" : false, "id" : 1, "text" : "Buy milk"};
var todo2 = {"completed" : false, "id" : 2, "text" : "Make dinner"};
var todo3 = {"completed" : false, "id" : 3, "text" : "Save the world"};


//*****I have inserted all elements in db once*******
// collection.insert([todo1, todo2, todo3], function (err, result) {
//       if (err) {
//         console.log(err);
//       } else {
//         console.log('Inserted %d documents into the "my_todos" collection. The documents inserted with "_id" are:', result.length, result);
//       }
// });

// collection.find().toArray(function (err, result) {
//       if (err) {
//         console.log(err);
//       } else {
//         console.log('Found:', result);
//       }
// });

//*************************************************

var express = require('express');
var bodyParser = require('body-parser');
var app = express();
app.use(bodyParser.urlencoded());
app.use(bodyParser.json());
app.use(express.static('./public/assets'))

//*********************select**********************

 app.get('/todos', function(req, res){
   collection.find().toArray(function (err, result) {
         if (err) {
           console.log(err);
         } else {
           console.log('Found:', result);
         }
         res.send(result);
       });
   });

//**************************************************

  // app.get('/todos/:id', function(req, res){
  //   res.send(collection.find({id:req.params.id}).toObject());
  //   // collection.find({completed: false}).toArray(function(err, result){
  //   //       if (err) {
  //   //         console.log(err);
  //   //         return;
  //   //       }
  //   //       res.send(result[0]);
  //   //     });
  //   });

  // app.get('/todos/:id', function(req, res){
  //   var req_id = parseInt(req.params._id)
  //   collection.find({id: req_id}).toArray(function(err, result){
  //          if (err) {
  //           console.log(err);
  //           return;
  //           }
  //           res.send(result);
  //         });
  // });

  app.get('/todos/:id', function(req, res){
    console.log(req.params.id);
    collection.find({id: req.params.id}).toArray(function(err, result){
           if (err) {
            console.log(err);
            return;
            }
            res.send(result);
          });
});
//*****************post*(insert)******************

cb = collection.count({}, function(error, numOfDocs){
    var size = numOfDocs;
});

app.post('/todos', function(req, res){
  collection.insert({text: req.body.text}, function(err, result){
    result = {};
    //result.id = size;
    result.id = req.params.id;
    result.text = req.body.text;
    result.completed = "false";
    res.send(result);
  })
});

//********************put*(update)****************

app.put('/todos/:id', function(req, res){
  collection.update({_id:req.params.id}, {completed:"true"}, function(err, result){
    if(err){
      console.error(err);
      return;
    }
    result = {};
    result.id = req.params.id;
    result.text = req.body.text;
    result.completed = "true";
    res.send(result);
  });
});


//*****************************delete******************************
//
// //only updates
// // app.delete('/todos/:id', function(req, res){
// //   connection.query('update todos set destroyed = "true" where id = ?', req.params.id, function (err, result) {
// //       if (err) throw err;
// //       console.log('Changed ' + result.affectedRows + ' rows');
// //       result = {};
// //       result.id = req.params.id;
// //       result.text = req.body.text;
// //       result.completed = req.params.completed;
// //       result.destroyed = "true";
// //       console.log(result);
// //       res.send(result);
// //   });
// // });
//
// //removes
// app.delete('/todos/:id', function(req, res){
//   connection.query('delete from todos where id = ?', req.params.id, function (err, result) {
//       if (err) throw err;
//       console.log('Changed ' + result.affectedRows + ' rows');
//       result = {};
//       result.id = req.params.id;
//       result.text = req.body.text;
//       result.completed = req.params.completed;
//       result.destroyed = "true";
//       console.log(result);
//       res.send(result);
//   });
// });

app.listen(3000);

// db.close();
 }
});
