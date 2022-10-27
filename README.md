# DDF Service
A simple DDF Study Definitions Repository (SDR) Simulator. A simple micro service that emulates the TransCelerate SDR functionality and provides the current API specification

# Example Files
See the json files within the study directory

# Docker
## How to build the image
```
docker build --pull --rm -f "Dockerfile" -t ddfservice:latest "." --build-arg DDF_SERVICE_PROJ_KEY_ARG=<DDFServiceProjectKey>
```

## How to build the container
```
docker container run -p 80:80 -dit --name ddf ddfservice:latest
```