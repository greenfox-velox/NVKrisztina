//This code is the material from a YouTube tutorial
//codecast, this is not my code.

var mysql = require('mysql');

var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'monochrome',
  database: 'articles'
});
connection.connect();

connection.query('select * from articles', function(err, result){
  console.log(result);
})

//var id = '1; drop table articles'
//'select * from articles where id = ' + connection.escape(id), function(err, result)
