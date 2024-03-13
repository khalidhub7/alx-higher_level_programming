#!/usr/bin/node

/* function return reversed of list */

exports.esrever = function (list) {
  let i = list.length - 1;
  rev = [];
  while (i >= 0) {
    rev.push(list[i]);
    i--;
  }
  return rev;
};
