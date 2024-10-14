FROM python:3.11-slim

WORKDIR /app

COPY . /app/
COPY .env /app/.env.docker

RUN pip install -r requirements.txt --verbose


CMD python manage.py migrate \
    && python manage.py collectstatic --no-input \
    && uvicorn config.asgi:application --host 0.0.0.0 --port 8000
