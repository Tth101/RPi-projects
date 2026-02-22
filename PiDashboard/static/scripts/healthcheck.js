const TABLE_BODY = document.getElementById("hcTableBody");
const THROBBER_DIV = document.getElementById("throbberDiv");

function showThrobber() {
    THROBBER_DIV.style.zIndex = "1000";
}

function hideThrobber() {
    THROBBER_DIV.style.zIndex = "-1";
}

function healthcheck() {
    showThrobber();
    fetch("http://localhost:8080/hc/new")
    .then(res => {
        res.json().then(data => {
            document.getElementById("lastUpdate").innerText = new Date().toLocaleString();
            populateHealthcheckTable(data)
            hideThrobber();
        })
    });
}

function getLatestHealthcheck() {
    showThrobber();
    fetch("http://localhost:8080/hc/latest")
    .then(res => {
        res.json().then(data => {
            document.getElementById("lastUpdate").innerText = data.Datetime;
            populateHealthcheckTable(JSON.parse(data.JSON))
        })
    })
    hideThrobber();
}

function populateHealthcheckTable(data) {
    TABLE_BODY.innerHTML = "";
    data.forEach((endpoint, index) => {
        //Endpoint object has Name, URL, Health, StatusCode, Err
        var healthCol = "";
        switch(endpoint.Health) {
            case "Up":
                healthCol = `&#128994; (${endpoint.StatusCode})`;
                break;
            case "Down":
                healthCol = `&#128308; (${endpoint.StatusCode})`;
                break;
            default:
                healthCol = `
                    <div id="errStatusDiv">&#10071;(${endpoint.StatusCode})</div>
                    <div id="errMsgDiv">${endpoint.Err}</div>
                `;
        }

        tr = document.createElement("tr");
        tr.innerHTML = `
            <th scope="row">${index}</th>
            <td><a href="${endpoint.Url}">${endpoint.Name}</a></td>
            <td>${healthCol}</td>
        `;
        TABLE_BODY.appendChild(tr);
    });
}