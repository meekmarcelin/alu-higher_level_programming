#!/usr/bin/node
module.exports = class square extends require('./5-square.js') { charPrint (c) { if (c === unidefined) { c = 'X'; } for (let i = 0; i < this.height; i++) { console.log(c.repeat(this.width)); } } };
