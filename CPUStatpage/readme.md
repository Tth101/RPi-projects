# CPU Stats Web Page (Project 1)
This project was done with portainer and docker in a Raspberry Pi, with the goal of being able to display various CPU statistics on a web page \
*As this is my first project, any information/code will be very prone to errors and misconfigurations.*

## Overview
In this project, the aim will be to set up a container in docker with the files in this github repo, allowing us to run a web app which displays CPU stats obtained from various commands 

## Project folder structure


## Topology
![alt text](topology.png)

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
```

## Important tip(s)
1. Do not name your `WORKDIR` in `dockerfile` the same as your folders in your project repo: troubleshooting will be quit difficult
