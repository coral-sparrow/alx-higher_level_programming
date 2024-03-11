#!/usr/bin/node

// import { argv } from 'node:process';
const { argv } = require('node:process');

const numberOfOccurrence = Number(argv[2]);
if (numberOfOccurrence) {
  for (let i = 0; i < numberOfOccurrence; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
