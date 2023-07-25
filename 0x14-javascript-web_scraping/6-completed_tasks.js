#!/usr/bin/node

const request = require('request');
let results;

req(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const new_obj = {};
  results = JSON.parse(body);

  for (const result of result) {
    const user = result.userId;
    new_obj[user] = 0;
  }

  for (const result of results) {
    const user = result.userId;
    if (result.completed === true) {
      new_obj[user] += 1;
    }
  }

  console.log(new_obj);
});
