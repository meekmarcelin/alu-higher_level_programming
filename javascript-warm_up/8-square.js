#!/usr/bin/node 
const arg = parseInt(process.argv[2]);
if (!arg) { console.log('Missing size'); }
for (let i = 0; i < arg; i++) { console.log('X'.repeat(arg)); }
