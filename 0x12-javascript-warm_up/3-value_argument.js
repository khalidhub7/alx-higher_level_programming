#!/usr/bin/node
const { argv } = require('node:process');
let number_of_args_passed = 0;
argv.forEach((value, key) => {
  if (key === 2) {
    console.log(`${value}`);
  }
  number_of_args_passed++;
});
if (number_of_args_passed === 2) {
  console.log('No argument');
}
