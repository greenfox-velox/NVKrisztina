var mysql = require('mysql');

var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'monochrome',
  database: 'todos'
});
connection.connect();

connection.query('select * from todos', function(err, result){
  console.log(result);
})
