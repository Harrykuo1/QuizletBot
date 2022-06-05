FROM selenium/standalone-chrome-debug

USER root
RUN apt-get update
RUN apt-get install -y python3-pip

COPY ./ecourseRequirement.txt ecourseRequirement.txt
RUN pip3 install -r ecourseRequirement.txt

WORKDIR /ecourse