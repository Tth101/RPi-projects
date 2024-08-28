function refresh_variables() {
    fetch('../CPUStatpage.py')
    .then(response => response.json())
        .then(data => {
         // Display the result from the Python function
         document.getElementById('temperature').innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}