#Attempt 3
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /code/

#cd to folder, run "docker build ." or "docker build -t projectphase:1.0 ." <- specifes tag 
#run "docker images" to view images & get its ID
#run "docker run *IMAGE ID*"