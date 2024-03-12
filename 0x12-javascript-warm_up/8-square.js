#!/usr/bin/node

const { argv } = require('node:process');
let num;
argv.forEach((value, key) => {
  if (key === 2) {
    num = value;
    if (isNaN(num)) {
      console.log('Missing size');
    }
  }
});
let i = 0;
while (i < num) {
  console.log('X'.repeat(num));
  i++;
}
