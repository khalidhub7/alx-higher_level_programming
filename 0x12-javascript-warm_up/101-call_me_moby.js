#!/usr/bin/node

function callMeMoby (x, theFunction) {
  let i = 0;
  while (i < x) {
    theFunction();
    i++;
  }
}

callMeMoby.exports;
