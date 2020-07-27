const express = require('express')
const {spawn} = require('child_process');
var bodyParser = require('body-parser');
var path = require('path');
const app = express()
const port = 3000
// for parsing application/json
app.use(bodyParser.json()); 

// for parsing application/xwww-
app.use(bodyParser.urlencoded({ extended: true })); 
//form-urlencoded


app.get('/', function(req, res) {
	res.sendFile(path.join(__dirname + '/public/index.html'));
});
app.post('/move', function(req, res) {
 console.log(req.body)
 const python = spawn('python', ['servo.py', req.body.x, req.body.y]);
 python.on('close', (code) => {
 console.log(`child process close all stdio with code ${code}`);
 res.send('done')
 //res.sendFile(path.join(__dirname + '/public/index.html'));
});
});
app.listen(port,'0.0.0.0', () => console.log(`Example app listening on port 
${port}!`))
