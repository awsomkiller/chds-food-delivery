from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

CORS_ALLOW_HEADERS = [
    "ngrok-skip-browser-warning",
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
    "access-control-allow-origin",
    "Authorization",
]

ALLOWED_HOSTS = [
    "chds.com.au",
    "api.chds.com.au",
    "170.64.235.98",
    "localhost"
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}


CSRF_TRUSTED_ORIGINS = [
    "https://www.chds.com.au",
    "https://chds.com.au",
]

CORS_ALLOWED_ORIGINS = [
    "https://www.chds.com.au",
    "https://chds.com.au",
]

CORS_ORIGIN_WHITELIST = (
    "https://www.chds.com.au",
    "https://chds.com.au",
)

MEDIA_ROOT = os.path.join("/","var","www","media")
STATIC_ROOT = os.path.join("/","var","www","static")