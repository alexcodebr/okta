

var tables = [
    { "art":"A","count":"0","name":"name1","ean":"802.0079.127","marker":"null","stammkost":"A","tablename":"IWEO_IWBB_01062015" },
    { "art":"A","count":"0","name":"2","ean":"657.7406.559","marker":"null","stammkost":"A","tablename":"IWEO_IWBB_02062015" }
];

tables.forEach(function(table) {
    var tableName = table.name;
    console.log(tableName);
});

