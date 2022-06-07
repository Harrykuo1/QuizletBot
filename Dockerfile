FROM python:3.9.12-buster

USER root
RUN apt-get update -y
RUN apt-get install -y python3-pip
RUN apt-get install -y tesseract-ocr
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r  /requirements.txt 

WORKDIR /app