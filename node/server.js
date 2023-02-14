const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');

http.createServer((req, res) => {
  if (req.url === "/") {
      fs.readFile("./public/index.html", "UTF-8", (err, body) => {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  } else if(req.url.match("/sysinfo")) {
    myHostName=os.hostname();
	//get total uptime and convert into days, hours, minutes, and seconds
	uptime = os.uptime();
	var uptimeDays = Math.floor(uptime/86400);
	var uptimeHours = Math.floor((uptime - uptimeDays * 86400) / 3600);
	var uptimeMinutes = Math.floor((uptime - uptimeDays * 86400 - uptimeHours * 3600) / 60);
	var uptimeSeconds = Math.floor(uptime - uptimeDays * 86400 - uptimeHours * 3600 - uptimeMinutes * 60);
	
	//get total memory and convert to MB
	var totalByte = os.totalmem();
	var totalMegaBit = totalByte * 0.000001
	
	//get free memory and convert into MB
	var freeByte = os.freemem();
	var freeMegaBit = freeByte * 0.000001
	
	//get number of CPU's
	var cpus = os.cpus().length;
	
    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Uptime: Days: ${uptimeDays}, Hours: ${uptimeHours}, Minutes: ${uptimeMinutes}, Seconds: ${uptimeSeconds}</p>
        <p>Total Memory: ${totalMegaBit} MB</p>
        <p>Free Memory: ${freeMegaBit} MB</p>
        <p>Number of CPUs: ${cpus}</p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");