#!/bin/bash
psql postgres -h localhost -p 5432 -U postgres -f /code/extensions.sql
osm2pgsql -E 3857 --cache-strategy sparse -d postgres -H localhost -U postgres -P 5432 --hstore --hstore-add-index /code/laPlata.osm
psql postgres -h localhost -p 5432 -U postgres -f /code/ids.sql