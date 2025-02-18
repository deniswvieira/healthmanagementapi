from .base import *

DEBUG = True

SECRET_KEY = "django-insecure-=-+y&n4v0)p#l)@uq&0u(2!mbt*m3ibmi$)!njd2*ua4w+$g8n"

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
