FROM python:3.13-slim

WORKDIR /app

COPY carnival_ops/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY carnival_ops/ .

EXPOSE 8000

# Development server - replace with gunicorn for production
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
