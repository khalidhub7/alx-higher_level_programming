#!/usr/bin/node

const { argv } = require('node:process');
let num;
argv.forEach((value, key) => {
  if (key === 2) {
    num = value;
    if (isNaN(num)) {
      console.log('Missing number of occurrences');
    }
  }
});
let i = 0;
while (i < num) {
  console.log('C is fun');
  i++;
}
