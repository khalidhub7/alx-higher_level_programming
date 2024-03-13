#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = Square;

class Square extends Rectangle {
  constructor (size) {
    super();
    this.width = size;
    this.height = size;
  }
}
