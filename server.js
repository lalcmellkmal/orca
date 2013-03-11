var connect = require('connect'),
    exec = require('child_process').exec;

const HEAD = '<!doctype html>\n<meta charset=utf8>\n<title>O.R.C.A.</title>\n<link rel=stylesheet href=v1.css>\n';
const BIN = require('path').join(__dirname, 'story.py');

var app = connect();
app.use(function (req, resp, next) {
	if (req.url == '/') {
		resp.writeHead(200, {
			'Cache-Control': 'no-cache',
			'Content-Type': 'text/html; charset=UTF-8',
			'Expires': 'Thu, 01 Jan 1970 00:00:00 GMT',
		});
		if (req.method == 'HEAD')
			return resp.end();

		resp.write(HEAD);
		exec(BIN, function (err, stdout, stderr) {
			if (!err && !stderr) {
				resp.end(connect.utils.escape(stdout));
				return;
			}
			console.error(err, stdout, stderr);
			resp.end("<i>Some error occurred. Try again later.</i>\n");
		});
		return;
	}
	next();
});

app.use(connect.static('pub'));
app.listen(8000);
