#!/usr/bin/node
const { argv } = require('node:process');
let num;
let arg;
argv.forEach((value, key) => {
  if (key === 2) {
    arg = value;
  }
  num = Number(arg);
});

if (argv.length === 2) {
  console.log('Not a number');
} else if (!isNaN(num)) {
  console.log('My number: ' + `${parseInt(num)}`);
} else {
  console.log('Not a number');
}
