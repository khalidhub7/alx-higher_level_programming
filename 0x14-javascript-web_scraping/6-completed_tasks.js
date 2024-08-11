#!/usr/bin/node

const requesttool = require('request');
const url = process.argv[2];

function completedtasks (url) {
  requesttool(url, (err, Response, body) => {
    if (err) {
      console.log(err);
      return;
    }
    const data = JSON.parse(body);
    const tasks = {};
    let i = 0;

    while (i < data.length) {
      const userId = data[i].userId;
      if (data[i].completed === true) {
        if (!tasks[userId]) {
          tasks[userId] = 0;
        }
        tasks[userId] += 1;
      }
      i++;
    }
    console.log(tasks);
  });
}
completedtasks(url);
