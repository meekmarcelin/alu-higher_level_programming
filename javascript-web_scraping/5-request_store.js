#!/usr/bin/node
const fs = require('fs');
require('request').get(process.argv[2], (err, response, body) => {
  if (err) console.log(err);
  fs.writeFile(process.argv[3], body, (error, res) => {
    if (error) console.log(error);
  });
});
