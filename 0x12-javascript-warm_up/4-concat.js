#!/usr/bin/node
const { argv } = require('node:process');
let value1;
let value2;
argv.forEach((value, key) => {
  if (key === 2) {
    value1 = value;
  }
  if (key === 3) {
    value2 = value;
  }
});
if (argv.length === 2) {
  console.log('undefined is undefined');
} else if (argv.length === 3) {
  console.log(value1 + ' is undefined');
} else if (argv.length === 4) {
  console.log(value1 + ' is ' + value2);
}
