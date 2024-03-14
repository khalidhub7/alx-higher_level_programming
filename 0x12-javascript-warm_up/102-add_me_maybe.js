#!/usr/bin/node

exports.addMeMaybe = function (number, theFunction) {
  /* Increment number and pass it to theFunction */
  theFunction(++number);
};

