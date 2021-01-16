# CovidWebApp-ML

## Overview
The Machine Learning component for the CovidWebApp project for Software Technologies 2020/2021.

Link to the [Web UI component](https://github.com/Boyannik7/CovidWebApp-front-end)

Link to the [Server component](https://github.com/Boyannik7/CovidWebApp-server)

## Deployment and operation

This application is deployed using [Docker](https://www.docker.com/) either locally or on a 
[PaaS](https://azure.microsoft.com/en-us/overview/what-is-paas/) environment, such as [Cloud Foundry](https://www.cloudfoundry.org/)
or a container orchestration system like [Kubernetes](https://kubernetes.io/).

- To use the ML script as a standalone application, do the following:

---
### Prerequisite
To be able to build the docker image, you need Docker installed on your machine.

If you are using Windows or Mac, you can download [Docker Desktop](https://www.docker.com/products/docker-desktop).

If you are using a Linux distribution, use your appropriate package manager.

---

To build the docker image use:
```
docker build -t ml-script:latest https://github.com/Boyannik7/CovidWebApp-ML.git#main
```
To start the container use:
```
export VOLUME=<local path to store volume data>
docker run -p 80:8080 -v $VOLUME:/data \
    -e OUTPUT_DATA_FILE_NAME=../data/output_data \
    ml-script:latest
```

The ML script will be available to serve traffic at `http://<localhost | public domain>/`

---

- To use the whole project, follow the instructions from the [Server component](https://github.com/Boyannik7/CovidWebApp-server)
