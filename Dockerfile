# Use an official Python runtime as a parent image
FROM python:3.7-alpine

# Define environment variable
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

MAINTAINER Piyush0074

COPY ./requirements.txt /requirements.txt


# Install any needed packages specified in requirements.txt
RUN  pip install -r requirements.txt


RUN  mkdir /log

# Set the working directory to /log
WORKDIR /log

# Copy the current directory contents into the container at /log
COPY ./log /log

RUN adduser -D user
USER user





