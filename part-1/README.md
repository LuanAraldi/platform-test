# Platform test Part 1/2

This part of the test consists in constructing a web api, that is capable of ignoring requests with same body in a short timespan (10 minutes).

It was built using Node.js because of its good performance with IO interactions.

As a database, it was chosen MongoDB, for its good relationship with Node.js technologies and because it's a NoSQL alternative

## Prerequisites
- [Docker]{https://docs.docker.com/install/}
- [Docker Compose]{https://docs.docker.com/compose/install/}

## Running tests

There is a specially created compose file (to make things easier) for testing purposes, look below to see how to run it
```bash
docker-compose -f docker-compose.test.yml up --build
```

## Running the application

- Run swarm configuration script
To run locally, follow scenario A
This script takes care of creating networks, registry services, building compose stack and deploying it to the local registry.
If the app will be deployed to real production environments, scenario B should be followed.

Scenario A:
```bash
./setup-swarm.sh
```

Scenario B:
Change registry location on docker-compose.yml file, like the example below
```yml
web:
    image: <registry_url>:<registry_port>/stackplat
    build: .
```
And then
```bash
docker-compose build
docker-compose push
```

- Run MongoDB
```bash
docker run -it --hostname mongodb --name=mongodb --net=dockernet --expose=27017 mongo:3.4.19-jessie
```

- Check MongoDB IP Address
This only applies if mongo is running in a docker container aswell, inside the app machine, otherwise, the mongoDB exposed IP Address should be used
```bash
docker inspect mongodb | grep IPAddress
```

- Place MongoDB IP Address on docker-compose.yml, on environment variables, like the example below
```yml
services:
  web:
    build: ./
    environment:
      - MONGO_IP=192.168.0.2
    command: npm run start
    ports:
      - "3000:80"
    networks:
      - dockernet
```

- Run application in swarm mode
```bash
    docker stack deploy --compose-file docker-compose.yml plat-stack
```