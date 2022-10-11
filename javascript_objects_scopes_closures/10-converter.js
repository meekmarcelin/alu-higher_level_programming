#!/usr/bin/node
exports.converter = function (base) { return (num) => { return num.tostring(base); }; };
