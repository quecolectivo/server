## Backend server for quecolectivo built on top of django.

[![Gitter](https://badges.gitter.im/Join Chat.svg)](https://gitter.im/quecolectivo/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)


### Docker dev setup assuming you have `docker` and `docker-compose` already installed on your system:
    
- `docker-compose build`

    downloads the images and builds the container

- `docker-compose run --rm django bash initdb/init.sh` 

    this populates the db with data and sets up postgis. change the default .osm file accordingly for whatever zone you prefer, as well as the db name, etc.

- `docker-compose up`

    your project should be up on localhost:8000, you can try to make a query like:
    [http://localhost:8000/api/search/-34.894461,-57.976782/-34.894461,-57.976782/100/](http://localhost:8000/api/search/-34.894461,-57.976782/-34.894461,-57.976782/100/)
  


### local dev setup:
    TODO


### deploy to production
    
- need to define the following env variables: ` POSTGRES_USER, PGPASSWORD, DJANGO_SECRET_KEY `

   you can do
   ```
   export PGPASSWORD=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 80 ; echo '')
   export DJANGO_SECRET_KEY=$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 80 ; echo '')

   echo "PGPASSWORD=$PGPASSWORD"
   echo "DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY"
   ``` 

- create a new amazonec2 instance with  
    `docker-machine create --driver amazonec2 --amazonec2-region sa-east-1 quecolectivo`

- to connect to the remote docker container run  
    `eval $(docker-machine env quecolectivo)`

- continue similar to the dev setup but use the docker-compose-prod file
    ```
    docker-compose -f docker-compose-prod.yml build
    
    docker-compose -f docker-compose-prod.yml run --rm django bash initdb/init.sh
    
    docker-compose -f docker-compose-prod.yml up
    ``` 


### Project structure
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
