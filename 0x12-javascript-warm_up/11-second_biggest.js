#!/usr/bin/node

const { argv } = require('node:process');
const mylist = [];
let nums = 0;

/* extract elements in command line */
argv.forEach((value, key) => {
    nums = value;
  mylist.push(Number(nums));
});

if (argv.length < 4) {
  console.log('0');
} else {
  const NewList = [];
  let i = 2;
  /* removing index 0 && index 1 in list  */
  while (i < argv.length) {
    NewList.push(mylist[i]);
    i++;
  }
  NewList.sort();
  NewList.reverse();
  console.log(NewList[1]);
}
