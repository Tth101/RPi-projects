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

    var f = evt.target.files[0];
                if (f) {
                    var r = new FileReader();
                    r.onload = function(e) { 
                        var contents = e.target.result;
                    }
                    r.readAsText(f);
                } else {
                    alert("Failed to load file");
                }