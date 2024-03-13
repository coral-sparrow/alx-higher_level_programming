#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let raw = '';

        for (let j = 0; j < this.width; j++) {
          raw += c;
        }

        console.log(raw);
      }
    }
  }
}

module.exports = Square;
