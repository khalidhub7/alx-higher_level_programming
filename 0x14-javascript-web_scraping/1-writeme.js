#!/usr/bin/node

const filepath = process.argv[2];
const filetool = require('fs');
const filecontent = process.argv[3];

function writefile (filepath) {
  filetool.writeFile(filepath, filecontent, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
      return 1;
    } else {
      return 0;
    }
  });
}
writefile(filepath);
