#!/bin/bash
psql -h $POSTGRES_HOST -p 5432 -U $POSTGRES_USER -c "CREATE DATABASE laplata;"
psql $POSTGRES_DATABASE -h $POSTGRES_HOST -p 5432 -U $POSTGRES_USER -f /code/extensions.sql
osm2pgsql -E 3857 --slim --cache-strategy sparse -d $POSTGRES_DATABASE -H $POSTGRES_HOST -U $POSTGRES_USER -P 5432 --hstore --hstore-add-index /code/laPlata.osm
psql $POSTGRES_DATABASE -h $POSTGRES_HOST -p 5432 -U $POSTGRES_USER -f /code/merge.sql