### Poll API

#### Technologies

- Python3.8+
- Poetry
- Fast API
- SQLAlchemy
- Postgres
- Uvicorn

#### Local Development

1. Clone this repo and `cd` into repo directory
2. Create virtual environment: `python -m venv venv`
3. Install dependencies: `poetry install`
4. Run the server: `poetry run uvicorn main:app --reload`
5. Access swagger at: http://localhost:8000/docs

#### Run with Docker

1. docker-compose up
2. Build docker image with Dockerfile

#### Run migration

`alembic upgrade head`
