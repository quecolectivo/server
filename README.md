## Backend server for quecolectivo built on top of django.

[![Gitter](https://badges.gitter.im/Join Chat.svg)](https://gitter.im/quecolectivo/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


### create the following .env files on your system containing sensible information:

 - djangoserver/.env
 
    ```
   DJANGO_SETTINGS_MODULE=quecolectivo.settings
   POSTGRES_DATABASE=<db-name> # name of the db
   POSTGRES_USER=postgres # db user
   POSTGRES_HOST=db # db for docker, or localhost if you are developing locally
   PGPASSWORD=<yourpassword> # password here
   ```
   
- djangoserver/quecolectivo/quecolectivo/settings_secret.py

    ```
    SECRET_KEY = <secret-key>  # replace with secret key
    ```

### Docker dev setup assuming you have `docker` and `docker-compose` already installed on your system:
    
- `docker-compose run --rm django bash initdb/init.sh` 

    this populates the db with data and sets up postgis. change the default .osm file accordingly for whatever zone you prefer, as well as the db name, etc.
- `docker-compose run --rm django python quecolectivo/manage.py makemigrations`    
- `docker-compose run --rm django python quecolectivo/manage.py migrate`    

    runs django migrations on the db, sets up django tables, etc.
- `docker-compose up`

    your project should be up on localhost:8000, you can try to make a query like:
    [http://localhost:8000/api/search/-34.894461,-57.976782/-34.894461,-57.976782/100/](http://localhost:8000/api/search/-34.894461,-57.976782/-34.894461,-57.976782/100/)
  


### local dev setup:
    TODO

### structure of the project 
```
├── LICENSE
├── README.md
├── db
│   └── Dockerfile
├── djangoserver
│   ├── Dockerfile
│   ├── initdb
│   ├── quecolectivo
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── migrations
│   │   │   ├── models.py
│   │   │   ├── query.py
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── manage.py
│   │   └── quecolectivo
│   │       ├── __init__.py
│   │       ├── settings.py
│   │       ├── settings_secret.py
│   │       ├── settings_secret.py.template
│   │       ├── urls.py
│   │       └── wsgi.py
│   ├── requirements.txt
│   └── wait-for-postgres.sh
├── docker-compose.yml
└── nginx
    └── Dockerfile
```

## Licence:

This is Free Software, published under the GPL v3 LICENSE

## How to contribute:

We would love contributions, just submit an issue or join us in gitter, if you have any suggestions, please let us know.
