#!/usr/bin/node

const { argv } = require('process');
const mylist = [];
let nums = 0;

/* extract elements in command line */
argv.forEach((value, key) => {
  if (key >= 2) { // Start from index 2 to skip the first two arguments
    mylist.push(Number(value));
  }
});

if (mylist.length < 2) { // Check if there are less than two numbers
  console.log('0');
} else {
  const sortedList = mylist.sort((a, b) => b - a); // Sort the list in descending order
  console.log(sortedList[1]); // Print the second largest number
}
