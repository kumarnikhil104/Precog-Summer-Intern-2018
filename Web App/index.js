var express = require('express');
var app = express();

const port = process.env.PORT || 8000;

app.use(express.static('public'));

app.listen(port, function(){
	console.log("On port 8000");
})