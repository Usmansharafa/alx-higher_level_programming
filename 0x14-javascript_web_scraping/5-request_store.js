#!/usr/bin/node

const fs = require("fs");
const req = require("request");
const fpath = process.argv[3];
const url = process.argv[2];

req(url, (error, res, body) => {
  if (error) {
    console.log(error);
  }
  const cont = body.toString();
  fs.writeFile(fpath, cont, "utf-8", (error) => {
    if (error) {
      console.log(error);
    }
  });
});
