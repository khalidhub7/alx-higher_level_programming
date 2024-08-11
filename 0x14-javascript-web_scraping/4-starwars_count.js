#!/usr/bin/node
const tool = require('request');
const url = process.argv[2];
const caracter = 'https://swapi-api.alx-tools.com/api/people/18/';

function countfilms(url) {
  tool(url, (err, response, body) => {
    if (err) {
      return console.error(err);
    }

    const data = JSON.parse(body).results;
    let count = 0;

    data.forEach(film => {
      if (film.characters.includes(caracter)) {
        count++;
      }
    });

    console.log(count);
  });
}

countfilms(url);
