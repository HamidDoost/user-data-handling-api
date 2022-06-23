# pull official base image
FROM python:3.10.1-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables for preventing python writing pyc files and caching stdout
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc \
    && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .