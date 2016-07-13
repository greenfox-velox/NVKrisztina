var mysql = require('mysql');

var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'kiwitorta9',
  database: 'articles'
});
connection.connect();

connection.query('DELETE FROM articles WHERE id = ?', [3],
  function (err, result) {
    if (err) throw err;
    console.log('Deleted ' + result.affectedRows + ' rows');
  }
);
