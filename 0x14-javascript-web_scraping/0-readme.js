#!/usr/bin/node

const filetool = require('fs');
const filepath = process.argv[2];

function readfile (filepath) {
  filetool.readFile(filepath, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
      return 1;
    } else if (!err) {
      console.log(data);
      return 0;
    }
  });
}
readfile(filepath);
