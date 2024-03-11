#!/usr/bin/node

// import { argv } from 'node:process';
const { argv } = require('node:process');

const size = Number(argv[2]);
if (size) {
  for (let j = 0; j < size; j++) {
    let square = 'X';
    for (let i = 1; i < size; i++) {
      square += 'X';
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
