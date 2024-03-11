#!/usr/bin/node

// import { argv } from 'node:process';
const { argv } = require('node:process');

let biggest = 0;
let secondBiggest = 0;
if (argv.lenght <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < argv.length; i++) {
    const n = Number(argv[i]);
    if (n) {
      if (n > biggest) {
        secondBiggest = biggest;
        biggest = n;
      } else if (n > secondBiggest) {
        secondBiggest = n;
      }
    }
  }
  console.log(secondBiggest);
}
