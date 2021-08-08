const express = require('express')
const mysql = require('mysql');
const ejs = require('ejs');
const bodyParser = require('body-parser');

const app = express()
const port = 4000

const connection = mysql.createConnection({
  host:'localhost',
  user:'root',
  password:'1234',
  database: 'school',
  port: '3306',
});

connection.connect();

app.engine('html', require('ejs').renderFile);
app.engine('workspace', require('ejs').renderFile);
app.set('view engine', 'html');
app.set('view engine', 'workspace');

app.use(express.static('html'));
app.use(express.static('workspace'));
app.use(bodyParser.urlencoded({
  extended: false,
}));

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}/login.html`)
})
