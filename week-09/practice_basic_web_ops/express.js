var express = require('express');

var app = express();

//we tell express we want to use ejs as our view engine:
app.set('view engine', 'ejs');
//middleware használatához use. Ha a browserbe irjuk h 127.../anything, akkor.
//Megadjuk a static files helyét (benne css). Ha kihagyom a /anything-et,
//minden browser parancshoz értődik
app.use('/anything', express.static('my_static_files'));

app.get('/', function(req, res){
  res.send('this is the homepage');
});

app.get('/contact', function(req, res){
  res.send('this is the contact page');
  //res.render('profile', {gs: req.query});
});

app.get('/profile/:name', function(req, res){
  res.send('You requested to see a profile with the name of ' + req.params.name)
});

app.get('/character2', function(req, res){
  res.sendFile(__dirname + '/profile2.html')
});

app.get('/character1/:name', function(req, res){
  var data = {book: 'East of Eden', age: 58, job: 'Inventor', hobbies: ['horse riding', 'inventing new gadgets', 'wondering']};
  res.render('profile', {person: req.params.name, data:data});
});


app.listen(3000);
