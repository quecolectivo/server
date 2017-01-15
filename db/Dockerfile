FROM mdillon/postgis
RUN apt-get update && apt-get -y install osm2pgsql
RUN mkdir /code
WORKDIR /code
ADD map.osm /code/