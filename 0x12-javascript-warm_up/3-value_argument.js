#!/usr/bin/node
const { argv } = require('node:process');
argv.forEach((value, key) => {
  if (key === 2) {
    console.log(`${value}`);
  } else if (key < 2) {
    console.log('No argument');
  } else {
    return 0;
  }
});
