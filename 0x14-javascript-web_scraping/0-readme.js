#!/usr/bin/node

const file_tool = require('fs');
const file_path = process.argv[2];

function read_file (file_path) {
  file_tool.readFile(file_path, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
      return 1;
    } else if (!err) {
      console.log(data);
      return 0;
    }
  });
}
read_file(file_path);
