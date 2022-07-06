# User data handling RESTful API

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

- [API Description](#API-Description)
- [List of Technologies](#List-of-Technologies)
- [Features](#Features)
- [Installation](#Installation)
- [Configuration Setup](#Configuration-Setup)
- [Usage](#Usage)
- [Testing](#Testing)
- [Design and Architecture](#Design-and-Architecture)
- [Deployment](#Deployment)
- [License](#License)
- [Contact Information](#Contact-Information)

---

## API Description

User data handling api is a RESTful API designed for managng data from experiments. This API enables users to add and retrieve data to and from a PostgreSQL database asyncronously.

---

## List of Technologies

I used the following technologies for creating user-data-api.
| Technology | Description | Version |
|------------|-------------------------------------------|--------|
| Python | Main programming language | 3.10.1 |
| FastAPI | A modern web framework for building API | 0.78.0 |
| SQLModel | Object Relational Mapping | 0.0.6 |
| PostgreSQL | Relational Database Management System | 14.4 |
| asyncpg | A database interface library for PostgreSQL and Python/asyncio | 0.25.0 |
| Alembic | Database migration tool | 1.8.0 |
| pgAdmin 4 | PostgreSQL Tools | 6.2 |
| Pytest | Testing Framework | 7.1.2 |
| Pytest-asyncio | Enabling asyncronous for testing framework | 0.18.3 |
| Docker | Containerization of app, database and database admin tools | 20.10.11 |
| OpenAPI | Testing API endpoints and documentation | 3.1.0 |
| Github Actions | Automation of workflows, CI | |
| Github Packages | Hosting and managing docker images | |

---

## Features

user-data-handling-api has number of good features as follows:

- Documentation
- Asynchronous API calls
- Asynchronous database operations
- Error handling
- Expressive use of HTTP status codes
- Log activity
- Express URLs with nouns rather than verbs
- Consistent code convention
- Scalable designed architecture
- Database migration
- Unit testing with async calls
- Production-ready docker images

---

## Installation

For installation please consider the following steps:

- Clone the repository from git [link to repository](https://github.com/HamidDoost/user-data-handling-api.git)

- Build docker image ($ docker-compose build)
- Start the docker image ($ docker-compose up)

---

## Configuration Setup

### Database migration

API features automatic asynchronous migration upon startup of the server.

for future migrations please run:

$ docker-compose exec web alembic revision --autogenerate -m "your message"
$ docker-compose exec web alembic upgrade head

### Database schema and access

To check database schema and access to it, please do the following steps:

pgAdmin:

- open 127.0.0.1:5050 in your browser
- Login to pgAdmin. username: root@root.com, password: root
- in pgAdmin create new server with following parameters. server name: yourchoice, server host: web-db, port:5432, database: postgres, username: postgres, password: postgres

Alternatively you can access database in terminal:

- $ docker exec -it user-data-handling-api_web-db_1 bash
- $ psql -U postgres

---

## Usage

Detailed documentation for usage of API is accessible thorugh integrated OpenAPI http://localhost:8004/docs

---

## Testing

To run unit tests please run the following command:

$ docker exec user-data-handling-api_web_1 python -m pytest .

or simply run:
$ docker-compose exec web pytest

For test coverage:
$ docker-compose exec web python -m pytest --cov="."

For generating HTML file for coverage:
$ docker-compose exec web python -m pytest --cov="." --cov-report html

I added linting through Github Actions on push and pull_requests.

---

## Database design and data modelling

user-data-handling-api has user and experiment data models in a schema that provides one to many relationship between user and experiment models. For creatn models, I used SQLModel which is based on Pydantic and SQLAlchemy.

---

## Microservice design and scalable architecture

user-data-handling-api is scalable and can be used as a microservice.

---

## Deployment

A docker image of API is stored on Github Packages and can be accessed:

https://github.com/hamiddoost/user-data-handling-api/packages

or

$ docker pull ghcr.io/hamiddoost/user-data-handling-api/user-data-handler:latest

---

## License

user-data-handling-api is licensed under MIT.

---

## Contact Information

My Github username is hamiddoost.
