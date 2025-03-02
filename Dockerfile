FROM ubuntu:latest

RUN apt update && \
    apt install -y \
    libreoffice \
    fonts-liberation \
    default-jre \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /data
WORKDIR /data