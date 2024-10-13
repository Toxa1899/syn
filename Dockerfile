FROM python:3.11-slim

WORKDIR /app

COPY . /app/
COPY .env /app/.env.docker

RUN pip install -r requirements.txt --verbose

# Установим ENTRYPOINT
ENTRYPOINT ["sh", "-c"]

# CMD будет содержать команды для выполнения
CMD "python manage.py migrate && python manage.py collectstatic --no-input && daphne -b 0.0.0.0 -p 8000 config.asgi:application"
