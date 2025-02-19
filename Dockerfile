FROM python:3.10

# Working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    nginx \
    && rm -rf /var/lib/apt/lists/*

# Install project manager Poetry
RUN pip install --no-cache-dir poetry

# Copy projec config files to container
COPY pyproject.toml poetry.lock ./

# Install depencendies without creating a virtualenv
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --without dev

# Copy ramaining Django code
COPY . .

# Prepare django project
RUN poetry run python manage.py collectstatic --noinput
# RUN poetry run python manage.py migrate

EXPOSE 8000

COPY /docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

# Define entry point
ENTRYPOINT ["/docker-entrypoint.sh"]
