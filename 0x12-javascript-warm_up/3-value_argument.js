#!/usr/bin/node
const { argv } = require('node:process');
/* args: number of args passed in command_line */
let args = 0;
argv.forEach((value, key) => {
  args++;
  if (key === 2) {
    console.log(`${value}`);
  }
});
if (args === 2) {
  console.log('No argument');
}
