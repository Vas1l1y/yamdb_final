# API of project "Yamdb_final".

###
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/Vas1l1y/yamdb_final/.github/workflows/yamdb_workflow.yml/badge.svg)
## Description

The Yamdb_final project is a modified YaMDB project.

It is available in a container and works with a postgresql database.


The YaMDB project collects user feedback on creations (Title).
The creations are divided into categories: "Books", "Films", "Music", etc.
The list of categories can be expanded by the administrator.

In each category there is information about the creations.
The creations themselves are not stored in YaMDB;
you cannot watch a movie or listen to music here.

A creation can be assigned a genre from the preset list.
New genres can only be created by the administrator.

Users can leave text reviews for creations
and rate the creation in the range from one to ten (an integer);
from user ratings, an average rating of the creation is formed - rating (integer).
A user can leave only one review per creation.

###
Full API documentation is available at endpoint:
>redoc/

## Examples of requests

- user registration *(POST)*
>api/v1/auth/signup/ 
>```
>{
>    "username": "my_username",
>    "email": "my_email"
>}
>```

- getting access JWT-token *(POST)*
>api/v1/auth/token/ 
>```
>{
>    "username": "my_username",
>    "comfirmation_code": "my_ecomfirmation_code"
>}
>```

## Technology

python:3.7-slim

postgres:13.0-alpine

Django 2.2.16

Django REST framework 3.2.14

Docker 20.10.21

## For launch

Container run
```
docker-compose up
```

Rebuild the container and run
```
docker-compose up -d --build
```

Perform migrations
```
docker-compose exec web python manage.py migrate
```

Сreate a superuser
```
winpty docker-compose exec web python manage.py createsuperuser
```

Collect static
```
docker-compose exec web python manage.py collectstatic --no-input
```

Project website
```
The project is available at http://localhost .
```

## Author Infra_sp2 project

https://github.com/Vas1l1y


###


## Authors YaMDB project

https://github.com/NotMainCode

https://github.com/Vas1l1y

https://github.com/SerMikh1981

