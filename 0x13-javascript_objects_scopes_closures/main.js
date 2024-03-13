#!/usr/bin/node
const Rectangle = require('./4-rectangle');

const r1 = new Rectangle(2, 3);
console.log('**** before rotate *****');
r1.print();
console.log('**** after rotate *****');
r1.rotate();
r1.print();

const r2 = new Rectangle(10, 5);

console.log('**** before douple *****');
r2.print();

console.log('**** after douple *****');
r2.duple();
r2.print();
