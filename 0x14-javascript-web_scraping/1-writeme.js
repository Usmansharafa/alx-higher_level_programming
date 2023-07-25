#!/usr/bin/node

const fs = require('fs');
const fpath = process.argv[2];
const content = process.argv[3];

fs.writeFile(fpath, content, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
