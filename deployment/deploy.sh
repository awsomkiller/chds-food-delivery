#!/bin/bash

# Navigate to deployment directory
cd "$(dirname "$0")"

# Pull latest changes (optional, if using CI/CD)
git pull origin main

# Build and start containers
docker-compose up -d --build

# Apply migrations
docker-compose exec backend python manage.py migrate

# Collect static files
docker-compose exec backend python manage.py collectstatic --noinput

# (Optional) Create a superuser
# docker-compose exec backend python manage.py createsuperuser

# Restart services to apply changes
docker-compose restart

echo "Deployment completed successfully."
