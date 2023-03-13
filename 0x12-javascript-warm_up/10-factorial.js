#!/usr/bin/node

const { argv } = require('process');

function factorial (n) {
  const num = parseInt(n);
  if (num === 1 || isNaN(num)) { return 1; } else { return num * factorial(num - 1); }
}

console.log(factorial(argv[2]));
