FROM python:latest
EXPOSE 8000
RUN apt-get update
RUN apt-get -y install binutils libproj-dev gdal-bin postgresql osm2pgsql
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1
ADD . /code/
