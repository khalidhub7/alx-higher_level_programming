#!/usr/bin/node
const args = process.argv.slice(2);
function secondBig (array) {
  let biggest = array[0];
  let secBiggest = -Infinity;
  if (array.length <= 1) {
    return (0);
  }
  for (let i = 1; i < array.length; i++) {
    const num = parseInt(array[i]);
    if (num > biggest) {
      secBiggest = biggest;
      biggest = num;
    } else if (num < biggest && num > secBiggest) {
      secBiggest = num;
    }
  }
  return (secBiggest);
}
console.log(secondBig(args));
