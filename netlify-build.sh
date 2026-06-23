#!/usr/bin/env bash
set -o errexit

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Loading portfolio data from fixture..."
python manage.py loaddata fixtures/portfolio_data.json

echo "Exporting static site for Netlify..."
python manage.py export_for_netlify

echo "Netlify build complete."
