import os

from .base import *

DEBUG = False

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "CHAVE_SUPER_SECRETA")

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["PGDATABASE"],
        "USER": os.environ["PGUSER"],
        "PASSWORD": os.environ["PGPASSWORD"],
        "HOST": os.environ["PGHOST"],
        "PORT": os.environ["PGPORT"],
    }
}

CSRF_TRUSTED_ORIGINS = [
    "https://healthmanagementapi-production.up.railway.app",
    "https://healthmanagementapi-dev.up.railway.app",
]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
