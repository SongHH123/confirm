const express = require('express')
const app = express()
const port = 4000
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'html');

app.use(express.static('html'));

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}/login.html`)
})
