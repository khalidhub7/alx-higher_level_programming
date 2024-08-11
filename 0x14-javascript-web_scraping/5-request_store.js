#!/usr/bin/node

const url = process.argv[2];
const filepath = process.argv[3];
const filetool = require('fs');
const requesttool = require('request');

function toafile (url, filepath) {
  requesttool(url, (err, response, body) => {
    if (err) {
      console.log(err);
      return;
    }

    const content = body;
    filetool.writeFile(filepath, content, err => {
      if (err) {
        console.log(err);
      }
      return 0;
    });
  });
}
toafile(url, filepath);
