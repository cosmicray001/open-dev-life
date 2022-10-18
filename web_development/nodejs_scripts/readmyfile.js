//read data from txt file as buffer

let fs = require("fs");

fs.readFile("myfile.txt", function (err, data) {
  if (err) throw err;
  console.log(data.toString());
});
