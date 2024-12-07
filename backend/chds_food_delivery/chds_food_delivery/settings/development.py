from .base import *


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
    "localhost",
    "127.0.0.1",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8080",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://localhost:8000",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:8000",
]

CORS_ORIGIN_WHITELIST = (
    "http://localhost:8080",
    "http://127.0.0.1:8080",
)

CORS_ALLOW_ALL_ORIGINS = True

MEDIA_ROOT = os.path.join(BASE_DIR,"media")
STATIC_ROOT = os.path.join(BASE_DIR,"static")