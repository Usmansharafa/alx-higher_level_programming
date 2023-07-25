#!/usr/bin/node

const req = require('request');
let results;

req(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const newObj = {};
  results = JSON.parse(body);

  for (const result of results) {
    const user = result.userId;
    newObj[user] = 0;
  }

  for (const result of results) {
    const user = result.userId;
    if (result.completed === true) {
      newObj[user] += 1;
    }
  }

  console.log(newObj);
});
