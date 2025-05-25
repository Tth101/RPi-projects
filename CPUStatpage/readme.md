# CPU Stats Web Page (Project 1)
This project was done with portainer and docker in a Raspberry Pi, with the goal of being able to display various CPU statistics on a web page \
*As this is my first project, any information/code will be very prone to errors and misconfigurations.*

## Overview
In this project, the aim will be to set up a container in docker with the files in this github repo, allowing us to run a web app which displays CPU stats obtained from various commands 

## Procedure
1. Hook up app.py to docker container using `docker-compose.yaml` & `dockerfile` and map ports to RPi to allow access from clients on the same network
2. Set up front end for testing purposes
3. Set up stats fetching 
* You will need to import the necessary volumes and devices to be able to run `vcgencmd measure_temp`
    ```
    volumes:
      - /usr:/usr

    environment:
      - LD_LIBRARY_PATH=/usr/lib

    devices:
      - /dev/vchiq
      - /dev/vcio
    ```
4. Set up SQLite3 database to store and retrieve data 
5. Style front end and present data

## Project folder structure
```
└── 📁CPUStatpage
    └── 📁app
        └── 📁static
            └── script.js
            └── styles.css
        └── 📁templates
            └── index.html
        └── app.py
        └── CPUStatpage.py
        └── dockerfile
        └── requirements.txt
    └── docker-compose.yaml
    └── topology.png
    └── readme.md
```

## Topology
![alt](topology.png)

* The app will refer to the required binaries and devices mounted onto the docker container to fetch the required information about the host's CPU
* Then, it will store the data in the sqlite.db file which is fetched to display on the website hosted by the app

## Socket mappings
RPi: 192.168.100.153 \
Web page container: 172.19.0.2 

172.19.0.2:5000 -> 192.168.100.153:8081


## Dependencies
*As of last commit on this specific project:*
```
python:3.12-slim (docker image)
flask
docker 27.1.2
portainer community edition 2.19.4
sqlite3 3.40.1
```

## Important tip(s)/Useful information/References
1. Do not name your `WORKDIR` in `dockerfile` the same as your folders in your project repo: troubleshooting will be quit difficult
2. Specifying volume in docker compose is `src path`:`dst path`
3. Develop the app first before implementing it (saves the 100+ commits and clearing of containers & images)
4. On python's `subprocess`: 
    * [Shell = true or Shell = false?](https://stackoverflow.com/questions/3172470/actual-meaning-of-shell-true-in-subprocess)
    * [Running commands](https://martinheinz.dev/blog/98)
5. Python's Regex `re.search` and `re.match` returns a `re.match` object. Use `groups()` or `group(index)` to obtain the plain values
6. Sqlite3 set up:
    * [Sqlite3 set up for RPi](https://pimylifeup.com/raspberry-pi-sqlite/)
    * [How to use flask with Sqlite3](https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3)
6. References:
    * [Similar project using Redis](https://github.com/tomnewport/rpi-docker-cpu-temperature-server)