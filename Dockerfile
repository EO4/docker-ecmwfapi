# alpine-python-ecmwfapi
FROM python:alpine

MAINTAINER epmorris "edward.morris@eo4.eu"

WORKDIR /usr/src/app

RUN pip install pytest-shutil
RUN pip install https://software.ecmwf.int/wiki/download/attachments/56664858/ecmwf-api-client-python.tgz

COPY . .

