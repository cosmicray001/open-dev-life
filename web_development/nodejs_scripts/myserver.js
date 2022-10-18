//create my server

let http = require("http");

http
  .createServer(function (req, res) {
    res.write("Hello from other side!");
    res.end();
  })
  .listen(8080, () => {
    console.log(`server start @ 8080`);
  });
