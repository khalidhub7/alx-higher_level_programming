#!/usr/bin/node

const tool = require('request');
const titleid = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + titleid;

function title (url) {
  tool(url, (err, response, body) => {
    if (!err) {
      console.log(JSON.parse(body).title);
    }
  });
}
title(url);
