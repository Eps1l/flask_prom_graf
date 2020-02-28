#!/bin/bash
app="docker.web"
docker stop ${app}
docker rm $(docker ps -a -q -f status=exited)
docker rmi ${app}
docker build -t ${app} .
docker run -d -p 56733:80 \
  --name=${app} \
  -v $PWD:/app ${app}
