#!/bin/bash
set -e  # Stop on error

# Build the project
echo "Building the project..."
pip install -r requirements.txt

# Make sure the static directory exists
echo "Creating static directories..."
mkdir -p static
mkdir -p staticfiles_build

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Run database migrations
echo "Running database migrations..."
python manage.py makemigrations
python manage.py migrate