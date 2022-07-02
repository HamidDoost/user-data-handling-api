# user-data-handling-api

API for data handling using FastAPI, SQLAlchemy, Alembic, JWT and Docker with CI

```
.
├── LICENSE
├── README.md
├── docker-compose.yml
└── src
    ├── Dockerfile
    ├── alembic.ini
    ├── app
    │   ├── __init__.py
    │   ├── api
    │   │   ├── __init__.py
    │   │   ├── health.py
    │   │   └── user.py
    │   ├── config.py
    │   ├── db.py
    │   ├── main.py
    │   └── models.py
    ├── db
    │   ├── Dockerfile
    │   └── create_db.sql
    ├── entrypoint.sh
    ├── migrations
    │   ├── README
    │   ├── env.py
    │   ├── script.py.mako
    │   └── versions
    │       └── 9f3411af692d_first_migration.py
    ├── requirements.txt
    └── tests
        ├── __init__.py
        ├── conftest.py
        └── test_health.py
```
