var mysql = require('mysql');

var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'monochrome',
  database: 'todos'
});
connection.connect();

connection.query('UPDATE todos SET completed = ? Where ID = ?', ["true", 5],
  function (err, result) {
    if (err) throw err;

    console.log('Changed ' + result.changedRows + ' rows');
  }
);
