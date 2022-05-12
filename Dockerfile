FROM python:3.9.12-buster

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r  /requirements.txt 

WORKDIR /app