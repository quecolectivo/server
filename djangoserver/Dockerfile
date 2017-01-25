FROM python:latest
EXPOSE 8000
RUN apt-get update
RUN apt-get -y install binutils libproj-dev gdal-bin postgresql osm2pgsql
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt
