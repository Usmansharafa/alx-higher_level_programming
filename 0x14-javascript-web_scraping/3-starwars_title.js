#!/usr/bin/node

const req = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

req(url, (error, res, body) => {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(body).title);
});
