#!/usr/bin/node

const { list } = require('./100-main');
let i = 0;
let mapping = [];
console.log(list);
mapping = list.map((x) => x * i++);
console.log(mapping);
