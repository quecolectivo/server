FROM python:latest
EXPOSE 8000
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get -y install binutils libproj-dev gdal-bin postgresql osm2pgsql
ENV PYTHONUNBUFFERED 1
ADD . /code/
