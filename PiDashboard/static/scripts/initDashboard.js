var URLs = {
    services: {},
    dashboards: {},
    information: {}
};
/*
Note this variable will be an object with the following properties: services, dashboards and information. 
Also note that the naming convention will follow that in the go file rather than the yaml itself
*/

async function initDashboard() {
    getLatestHealthcheck();
    await obtainURLs();
    populateDashboardDropdown();
    populateInformationDiv();
}

async function obtainURLs() {
    res = await fetch("http://localhost:8080/urls");
    data = await res.json();
    //By default should be capitalised for global scope in go
    URLs.services = data.Services;
    URLs.dashboards = data.Dashboards;
    URLs.information = data.Information;
}

function populateDashboardDropdown() {
    let dropdown = document.getElementById("dashboardDropdown");
    dropdown.innerHTML = '';
    for (const [key, value] of Object.entries(URLs.dashboards)) {
        let dashboardName = key;
        let dashboardURL = value;
        let html = `<li><a class="dropdown-item" href=\"${dashboardURL}\">${dashboardName}</a></li>`;
        dropdown.insertAdjacentHTML("beforeend", html);
    }
}

async function fetchInfoContent() {
    res= await fetch("http://localhost:8080/info")
    data = await res.json()
    return data;
}

async function populateInformationDiv() {
    let infoDiv = document.getElementById("infoDiv");
    let infoSourcesAndContent = await fetchInfoContent();
    infoSourcesAndContent.forEach(infoSource => {
        let infoSourceName = infoSource.Name;
        let infoSourceContent = infoSource.Content;
        let infoSourceUrl = infoSource.Url;
        let infoSourceErr = infoSource.Err;
        let infoSourceDiv = document.createElement("div");
        infoSourceDiv.classList.add("infoSrcDiv")
        console.log(infoSourceErr)
        infoSourceDiv.innerHTML = `<a href="${infoSourceUrl}"><h5>${infoSourceName}:</h5></a>`
        if(infoSourceErr.trim() != ""){
            infoSourceDiv.innerHTML += `<p class="infoSrcErr">Err: ${infoSourceErr}</p>`
        }
        else {
            infoSourceDiv.innerHTML += `<pre>${infoSourceContent}</pre>`
        }
        infoDiv.appendChild(infoSourceDiv);
    });
}