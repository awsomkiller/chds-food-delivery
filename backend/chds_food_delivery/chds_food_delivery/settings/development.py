
from .base import *


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.getenv("DB_NAME"),
#         "USER": os.getenv("DB_USER"),
#         "PASSWORD": os.getenv("DB_PASSWORD"),
#         "HOST": os.getenv("DB_HOST"),
#         "PORT": os.getenv("DB_PORT"),
#     }
# }
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
CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8080',
    'http://localhost:8080',
    'http://127.0.0.1:8000',
    'http://localhost:8000',
]

CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins (unsafe for production)
# Or explicitly specify allowed origins:
