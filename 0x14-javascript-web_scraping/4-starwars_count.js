#!/usr/bin/node
const tool = require('request');
const url = process.argv[2];
const caracter = 'https://swapi-api.alx-tools.com/api/people/18/';

function countfilms (url) {
  tool(url, (err, response, body) => {
    if (err) {
      console.log(err);
      return 0;
    }
    const data = JSON.parse(body).results;
    let i = 0;
    let j = 0;
    let count = 0;
    while (i < data.length) {
      while (j < data[i].characters.length) {
        if (data[i].characters[j] === caracter) {
          count += 1;
        }
        j++;
      }
      i++;
      j = 0;
    }
    console.log(count);
  });
}
countfilms(url);
