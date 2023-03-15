#!/usr/bin/node

const originalList = require('./100-data').list;
const newList = originalList.map((x, i) => x * i);

console.log(originalList);
console.log(newList);
