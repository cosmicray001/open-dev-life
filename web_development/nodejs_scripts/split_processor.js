//split a single Node process into multiple processes

let cluster = require("cluster");

if (cluster.isWorker) {
  console.log("I am a worker");
} else {
  console.log("I am a master");
  cluster.fork();
  cluster.fork();
}
