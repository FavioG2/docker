FROM nginx

MAINTAINER Favio Gonzalez

USER root

RUN apt-get update
RUN rm -v /etc/nginx/nginx.conf

ADD nginx.conf /etc/nginx/

