//This code is the material from a YouTube tutorial
//codecast, this is not my code.

var mysql = require('mysql');

var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'kiwitorta9',
  database: 'articles'
});

connection.connect();

var article = {
  author: 'Alex Booker',
  title: 'Node tutorial',
  body: 'foo bar'
};

var query = connection.query('insert into articles set?', article, function(err, result){
  if(err){
    console.error(err);
    return;
  }
  console.error(result);
});
