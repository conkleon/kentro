# Kentro – Carnival Ops

A Django application for managing carnival operations.

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (macOS / Windows) **or** Docker Engine (Linux)
  - **Docker Desktop must be running** before executing any `docker` or `docker compose` commands.
  - Verify Docker is running: `docker info`

## Quick Start with Docker

```bash
# Build and start the application
docker compose up --build

# The app will be available at http://localhost:8000
```

Run in the background:

```bash
docker compose up --build -d
```

Stop the application:

```bash
docker compose down
```

## Local Development (without Docker)

```bash
cd carnival_ops
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `DJANGO_SETTINGS_MODULE` | `carnival_ops.settings` | Django settings module |
| `ALLOWED_HOSTS` | `localhost,127.0.0.1` | Comma-separated list of allowed hostnames |
