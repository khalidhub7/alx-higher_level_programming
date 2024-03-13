#!/usr/bin/node

/* it is necessary to define i outside
 the function to give expected output */

let i = 0;
exports.logMe = function (item) {
  console.log(`${i}` + ': ' + `${item}`);
  i++;
};
