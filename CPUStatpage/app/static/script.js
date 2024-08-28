function refresh_variables() {
    var pythonscript = "../CPUStatpage.py"
    fetch('/init_stats')
    .then(response => response.json())
        .then(data => {
         // Display the result from the Python function
         document.getElementById('tmperature').innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}