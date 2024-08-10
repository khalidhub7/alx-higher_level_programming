#!/usr/bin/node

const tool = require('request');
const url = process.argv[2];

function showstatus (url) {
  tool(url, (err, response) => {
    if (!err) {
      console.log('code: ' + response.statusCode);
    }
  });
}
showstatus(url);
