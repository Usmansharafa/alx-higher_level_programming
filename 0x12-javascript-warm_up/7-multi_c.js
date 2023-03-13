#!/usr/bin/node

const { argv } = require('process');
if (!argv[2] || isNaN(parseInt(argv[2])) || parseInt(argv[2]) < 0) { console.log('Missing number of occurences'); } else {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    console.log('C is fun');
  }
}
