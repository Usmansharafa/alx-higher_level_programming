#!/usr/bin/node

const fs = require("fs");
const file_name = process.argv[2];
fs.readFile(file_name, "utf-8", (error, cont) => {
  if (error) {
    console.log(error);
  }
  console.log(cont.toString());
});
