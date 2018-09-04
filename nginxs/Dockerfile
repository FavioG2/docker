FROM nginx

MAINTAINER Favio Gonzalez

USER root

RUN apt-get update

ADD nginx.conf /etc/nginx/conf.d/default.conf
ADD web /usr/share/nginx/html/
ADD web /var/www/html

EXPOSE 90


