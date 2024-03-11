#!/usr/bin/node
const { argv } = require('node:process');
let number_of_args_passed = 0;
argv.forEach((value, key) => {
  number_of_args_passed++;
  if (key === 2) {
    console.log(`${value}`);
  }
});
if (number_of_args_passed === 2 || number_of_args_passed === 1) {
  console.log('No argument');
}
