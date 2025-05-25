# BME280 Web Page (Project 2)

## Overview
In this project, the aim of this project will be to deploy an app that makes use of the RPi and a BME280 sensor to measure information about the surroundings (temperature, humidity and pressure)

## Procedure
1. Connect the BME280 sensor to RPi's GPIO (follow the documentation)
2. Refer to Project 1 for basic project structure
3. Set up sensor data fetching  
4. Set up SQLite3 database to store and retrieve data 
5. Style front end and present data

## Project folder structure
```
└── 📁BME280
    └── 📁app
        └── app.py
        └── BME280.py
        └── dockerfile
        └── requirements.txt
        └── 📁static
            └── script.js
            └── styles.css
        └── 📁templates
            └── index.html
    └── docker-compose.yaml
    └── readme.md
```
## Topology
Refer to project 1's topology, it is pretty much the same

## Socket mappings
RPi: 192.168.100.153 \
Web page container:  

:5000 -> 192.168.100.153:8082

## Dependencies
*As of last commit on this specific project:*
```
python:3.12-slim (docker image)
flask
docker 27.1.2
portainer community edition 2.19.4
sqlite3 3.40.1
RPI.BME280 
```

## Important tip(s)/Useful information/References
1. [Setting up BME280 on RPi](https://randomnerdtutorials.com/raspberry-pi-bme280-python/)
2. [RPi pinout guide](https://randomnerdtutorials.com/raspberry-pi-pinout-gpios/)