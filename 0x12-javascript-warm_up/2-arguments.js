#!/usr/bin/node
const { argv } = require('node:process');
const args = argv.length - 2;
if (args === 0) {
	console.log('No argument');
}
if (args === 1) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}

