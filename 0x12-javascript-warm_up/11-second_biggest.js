#!/usr/bin/node

const { argv } = require('process');
const argLen = argv.length;
if (argLen === 2 || argLen === 3) { console.log(0); } else {
  const arr = argv.slice(2);
  console.log(secondMax(arr));
}

function secondMax (array) {
  const newArray = array.map((x) => parseInt(x));
  const max = Math.max(...newArray);
  let i = 0;
  let secMax = newArray[0];
  while (i + 1 < newArray.length) {
    if (newArray[i + 1] < secMax && secMax < max) { // pass
    } else { secMax = newArray[i + 1] === max ? secMax : newArray[i + 1]; }
    i++;
  }
  return secMax;
}
