const express = require('express')
const app = express()
const port = 4000
app.engine('html', require('ejs').renderFile);
app.engine('workspace', require('ejs').renderFile);
app.set('view engine', 'html');
app.set('view engine', 'workspace');

app.use(express.static('html'));
app.use(express.static('workspace'));

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}/login.html`)
})
