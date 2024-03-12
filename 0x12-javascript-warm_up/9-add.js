#!/usr/bin/node

const { argv } = require('node:process');
let num1;
let num2;
argv.forEach((value, key) => {
  if (key === 2) {
    num1 = value;
  }
  if (key === 3) {
    num2 = value;
  }
}
);
function add (a, b) {
  const res = a + b;
  if (argv.length <= 3) {
    console.log('NaN');
    return;
  }
  console.log(res);
}

add(Number(num1), Number(num2));
