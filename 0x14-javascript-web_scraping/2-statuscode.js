#!/usr/bin/node

const req = require("request");
const url = process.argv[2];

req(url, (error, res, body) => {
  if (error) {
    console.log(error);
  }
  console.log("code:", res.statusCode);
});
