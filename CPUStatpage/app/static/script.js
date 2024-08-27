const fs = require('node:fs');

para = document.getElementById('stats_para').innerHTML

//read and format file with CPU stats
fs.readFile('../stats.txt', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    else
    para = data
    });