#!/usr/bin/node

const { argv } = require('node:process');
const mylist = [];

/* extract elements in command line */
argv.forEach((value, key) => {
  /* Start from index 2 to skip the first two arguments */
  if (key >= 2) {
    mylist.push(Number(value));
  }
});

if (mylist.length < 2) {
  /* Check if there are less than two numbers */
  console.log('0');
} else {
  /* Sort the list in descending order */
  const sortedList = mylist.sort((a, b) => b - a);
  /* Print the second largest number */
  console.log(sortedList[1]);
}
