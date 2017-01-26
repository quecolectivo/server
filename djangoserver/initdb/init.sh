#!/bin/bash
psql postgres -h $POSTGRES_HOST -p 5432 -U $POSTGRES_USER -c "CREATE DATABASE ${POSTGRES_DATABASE};"
psql -d $POSTGRES_DATABASE -h $POSTGRES_HOST -p 5432 -U $POSTGRES_USER -f /code/initdb/extensions.sql
osm2pgsql --cache 100 -E 3857 --slim --cache-strategy sparse -d $POSTGRES_DATABASE -H $POSTGRES_HOST -U $POSTGRES_USER -P 5432 --hstore --hstore-add-index /code/initdb/laPlata.osm
psql -d $POSTGRES_DATABASE -h $POSTGRES_HOST -p 5432 -U $POSTGRES_USER -f /code/initdb/merge.sql