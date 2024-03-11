#!/usr/bin/node

// import { argv } from 'node:process';
const { argv } = require('node:process');

function add (a, b) {
  const aInt = Number(a);
  const bInt = Number(b);
  return aInt + bInt;
}

console.log(add(argv[2], argv[3]));
