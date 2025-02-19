#!/bin/bash

set -e

echo "Applying migrations..."
poetry run python manage.py migrate --no-input

# Ensure superuser exists. requires following environment variables:
# DJANGO_SUPERUSER_USERNAME
# DJANGO_SUPERUSER_PASSWORD
echo "Creating superuser..."
poetry run python manage.py createsuperuser --username "${DJANGO_SUPERUSER_USERNAME}" --no-input || true

echo "Initializing Gunicorn..."
exec poetry run gunicorn --bind 0.0.0.0:8000 settings.wsgi:application
