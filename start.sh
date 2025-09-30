#!/bin/sh

# Apply database migrations
python manage.py migrate

# Collect static files (if applicable)
#python manage.py collectstatic --noinput

# Start the Gunicorn server (or other WSGI server like uWSGI)
# Adjust the number of workers and bind address as needed
gunicorn your_project_name.wsgi:application --bind 0.0.0.0:$PORT
