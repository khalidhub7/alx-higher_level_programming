#!/usr/bin/node
const { argv } = require('node:process');
argv.forEach((value, key) => {
  if (key > 2) {
    console.log(`${value}`);
  } else {
    console.log('No argument');
  }
});
