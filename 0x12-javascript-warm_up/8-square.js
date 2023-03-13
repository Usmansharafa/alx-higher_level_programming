#!/usr/bin/node

const { argv } = require('process');
if (!argv[2] || isNaN(parseInt(argv[2]))) { console.log('Missing size'); } else if (parseInt(argv[2]) < 0) { // pass
} else {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    let square = '';
    for (let j = 0; j < parseInt(argv[2]); j++) { square += 'X'; }
    console.log(square);
  }
}
