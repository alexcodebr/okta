var fs = require('fs');
var json = JSON.parse(fs.readFileSync('loguser.json', 'utf8'));

console.log(json.eventType)
console.log(json.outcome.result)
console.log(Object.keys(json.debugContext.debugData))