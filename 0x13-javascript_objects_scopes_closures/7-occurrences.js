#!/usr/bin/node

/* function that returns the number of occurrences in a list */
exports.nbOccurences = function (list, searchElement) {
  let occurr = 0;
  let i = 0;
  while (i < list.length) {
    if (list[i] === searchElement) {
      if (list[i] === searchElement) {
        occurr++;
      }
    }
    i++;
  }
  return occurr;
};
