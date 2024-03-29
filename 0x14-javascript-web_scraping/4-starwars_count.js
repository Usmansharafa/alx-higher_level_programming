#!/usr/bin/node

const req = require('request');
const url = process.argv[2];
let count = 0;

req(url, (error, res, body) => {
  if (error) {
    console.log(error);
  }
  res = JSON.parse(body).results;
  for (const response of res) {
    if (response.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
