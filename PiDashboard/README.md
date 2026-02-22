# Home Dashboard

# Overview
This dashboard provides an overview of the services and some system info to aid in troubleshooting. It also contains links to other dashboards. The main purpose of this is to apply some new knowledge from my SWE intern and to improve troubleshooting speeds, as well as to have all my services accessible from one place

## Usage
* The navbar provides a dashboard dropdown, providing links to the service's dashboards (where applicable)
* The Services section provides an overlook of the services' health and provides the URL. The section will be refreshed every 5hrs and will store its information in a database. Refreshing it will run a healthcheck and re-verify the status of all services.
* The Information section will be fetched on every page reload. It is mainly for troubleshooting purposes

## Project folder structure
```
└── 📁PiDashboard
    └── 📁certs
        ├── local.crt
    └── 📁src
        ├── autoHC.go
        ├── customHTTPClient.go
        ├── dbActions.go
        ├── fetchInfo.go
        ├── go.mod
        ├── go.sum
        ├── handlers.go
        ├── HC.go
        ├── main.go
        ├── yamlProcessor.go
    └── 📁static
        └── 📁css
            ├── style.css
        └── 📁images
        └── 📁scripts
            ├── healthcheck.js
            ├── initDashboard.js
        ├── index.html
    ├── docker-compose.yaml
    ├── dockerfile
    ├── README.md
    └── URLs.yaml
```