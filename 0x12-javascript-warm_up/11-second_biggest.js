#!/usr/bin/node

const { argv } = require('process');
const mylist = [];

/* extract elements in command line */
argv.forEach((value, key) => {
  if (key >= 2) { // Start from index 2 to skip the first two arguments
    mylist.push(Number(value));
  }
});

if (mylist.length < 2) { // Check if there are less than two numbers
  console.log('0');
} else {
  /* Sort the list in descending order */
  mylist.sort();
  mylist.reverse();
  /* Print the second largest number */
  console.log(mylist[1]);
}
