#!/usr/bin/node

const { argv } = require('node:process');
let num;

argv.forEach((value, key) => {
  if (!argv[2]) {
    console.log('1');
    process.exit(0);
  }
  if (key === 2) {
    if (Number(value) === 0 || Number(value) === 1 ||
    isNaN(Number(value))) {
      console.log('1');
      process.exit(0);
    }
    num = Number(value);
  }
});

function fac (a) {
  if (a === 0 || a === 1) {
    return 1;
  }
  return a * fac(a - 1);
}

console.log(fac(num));
