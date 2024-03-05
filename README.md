# Project

https://github.com/TarasSavchyn/project.git


API for an application for leaving comments on the Django Rest framework, 
such technologies as Swagger, JWT Tokens, Docker, PostgreSQL are used.


## Content
- [technologies](#technologies)
- [documentation](#documentation)
- [using](#using)
- [get access](#using)
- [docker](#docker)
- [project developers](#project-developers)

## Technologies
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django-Rest-Framework](https://www.django-rest-framework.org/)
- [Swagger](https://swagger.io/)
- [Docker](https://www.docker.com/)


## Documentation
http://127.0.0.1:8000/api/doc/swagger/

http://127.0.0.1:8000/api/doc/redoc/

## Using
Clone the repository from GitHub:
```sh
$ git clone https://github.com/TarasSavchyn/project.git
```
Once you've cloned the repository, navigate into the repository.

Create a virtual environment and activate it using the following commands:
```sh
$ python3 -m venv venv
$ source venv/bin/activate
```

In directory backend create file ".env" with the following content:
```python
SECRET_KEY=django-insecure-5=6$k7w$$q_ks=zh%(!oer=$x=7*(cq)pxdpin@@koppqepe_6

POSTGRES_HOST=abul.db.elephantsql.com
POSTGRES_DB=ryhsjbpf
POSTGRES_USER=ryhsjbpf
POSTGRES_PASSWORD=Vjv0cg9zL4NpkbxTWaExXk6wkD5rt0L-

```
project/backend$ :
Backend:

```sh
$ pip install -r requirements.txt
```

```sh
$ python3 manage.py migrate
```

```sh
$ python3 manage.py runserver
```


## Docker
In directory create file ".env" with the following content:
```python
SECRET_KEY=django-insecure-5=6$k7w$$q_ks=zh%(!oer=$x=7*(cq)pxdpin@@koppqepe_6

POSTGRES_HOST=abul.db.elephantsql.com
POSTGRES_DB=ryhsjbpf
POSTGRES_USER=ryhsjbpf
POSTGRES_PASSWORD=Vjv0cg9zL4NpkbxTWaExXk6wkD5rt0L-

```
After that create the file "docker-compose.yml"
```python
version: "3.4"

services:
  backend:
    image: savik1992/project-backend:latest
    ports:
      - "8080:8080"
    command: sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8080"
    env_file:
      - .env
    depends_on:
      - db
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U habrpguser -d habrdb"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 10s
  db:
    image: postgres:14-alpine
    env_file:
      - .env

```

Then open your terminal and navigate to the directory you wish to store the project and run the following commands:
```sh
$ docker-compose up
```
Welcome, the application is ready to use at url http://localhost:8080/api/app

## Project developers

- [Taras Savchyn](https://www.linkedin.com/in/taras-savchyn-ba2705261/) — Python Developer


