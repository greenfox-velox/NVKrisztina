var mysql = require('mysql');

var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'kiwitorta9',
  database: 'articles'
});
connection.connect();

connection.query('UPDATE articles SET title = ? Where ID = ?', ["The martian", 5],
  function (err, result) {
    if (err) throw err;

    console.log('Changed ' + result.changedRows + ' rows');
  }
);
