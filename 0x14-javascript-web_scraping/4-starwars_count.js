#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const caracter = '/18/';

function countfilms (url) {
  request(url, (err, response, body) => {
    if (err) {
      console.error(err);
      return;
    }

    let count = 0;
    const { results } = JSON.parse(body);

    results.forEach(film => {
      film.characters.forEach(character => {
        if (character.includes(caracter)) {
          count++;
        }
      });
    });

    console.log(count);
  });
}

countfilms(url);
