FROM python

ADD flaskapp /flaskapp
RUN apt-get update
RUN python -m pip install --upgrade setuptools wheel 
RUN apt-get install --assume-yes python-virtualenv 
RUN cd flaskapp
RUN pip install flask
RUN pip install redis
RUN pip install -U flask_cors
RUN echo hola

EXPOSE 5000
