FROM selenium/standalone-chrome-debug

USER root
RUN apt-get update
RUN apt-get install -y python3-pip

COPY ./seleRequirement.txt seleRequirement.txt
RUN pip3 install -r seleRequirement.txt

WORKDIR /quizlet