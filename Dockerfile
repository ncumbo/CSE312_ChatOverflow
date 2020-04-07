#ATTEMPT 2
FROM nginx:alpine
COPY ../../p1/CSE312_ChatOverflow /usr/share/nginx/html

#delete all containers "docker rm -f $(docker ps -a -q)"


##ATTEMPT 1
#Getting base image ubuntu
#FROM ubuntu:18.04

#RUN apt-get update

#ENV HOME /
#WORKDIR /

#COPY . .

#EXPOSE 8000

#CMD ["echo", "Hello World!"]

#cd to folder, run "docker build ." or "docker build -t projectphase:1.0 ." <- specifes tag 
#run "docker images" to view images & get its ID
#run "docker run *IMAGE ID*"