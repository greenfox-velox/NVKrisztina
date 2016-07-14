var mysql = require('mysql');

var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'kiwitorta9',
  database: 'todos'
});
connection.connect();

connection.query('DELETE FROM todos WHERE id = ?', [3],
  function (err, result) {
    if (err) throw err;
    console.log('Deleted ' + result.affectedRows + ' rows');
  }
);
