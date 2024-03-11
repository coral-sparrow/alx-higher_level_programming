#!/usr/bin/node

// import { argv } from 'node:process';
const { argv } = require('node:process');

const n = Number(argv[2]);
function factorial (a) {
  if (!a) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
console.log(factorial(n));
