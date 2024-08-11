#!/usr/bin/node

const requesttool = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

function StarWarscharacters (url) {
  requesttool(url, (err, response, body) => {
    if (err) {
      console.log(err);
      return;
    }
    const data = JSON.parse(body).characters;
    const allcharacters = [];
    const i = 0;

    function fetchCharacter (i) {
      if (i >= data.length) {
        allcharacters.forEach(character => console.log(character));
        return;
      }
      const urll = data[i];
      requesttool(urll, (err, response, body) => {
        if (err) {
          console.log(err);
          return;
        }
        const newdata = JSON.parse(body).name;
        allcharacters.push(newdata);
        fetchCharacter(i + 1);
      });
    }

    fetchCharacter(i);
  });
}

StarWarscharacters(url);
