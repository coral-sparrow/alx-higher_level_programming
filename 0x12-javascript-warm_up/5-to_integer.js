#!/usr/bin/node

// import { argv } from 'node:process';
const { argv } = require('node:process');

const n = Number(argv[2]);
if (n) {
  console.log('My number:', n);
} else {
  console.log('Not a number');
}
