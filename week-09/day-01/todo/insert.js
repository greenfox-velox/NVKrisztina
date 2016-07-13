var mysql = require('mysql');

var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'kiwitorta9',
  database: 'todos'
});

connection.connect();

var todo1 = {
  id: 0,
  text: 'Play',
  completed: "false"
};


var query = connection.query('insert into todos set ?', todo1, function(err, result){
  if(err){
    console.error(err);
    return;
  }
  console.error(result);
});
