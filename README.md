# Astronomy API

## Description
With Python and Flask, endpoints obtain data through web scraping and store it in PostgreSQL and Redis (cache). Testing is done with Pytest and Postman, and everything runs in Docker. Also, return the data stored.

## Objective
The Objective of this project is to demonstrate abilities used in backend, testing and data processing.

## Installation
1. Resave any shell file (start.sh)

2. Build docker
```console
docker compose up --build -d
```

3. Go to Postman and test the endpoints or test them in a web browser

> **Note**: Be sure that you are in astronomers-api before executing all the commands.

## Possible errors
- exec /usr/local/bin/start.sh: no such file or directory
Resave the shell file because when making the start.sh file in Windows it creates a CRLF line ending file. Linux uses LF.
Resource: https://stackoverflow.com/questions/72735140/azure-agents-with-docker-start-sh-no-such-file-or-directory 

- port is already allocated
To fix it, it is necessary to change the port in the docker to another unoccupied or eliminate the container utilizing that port.