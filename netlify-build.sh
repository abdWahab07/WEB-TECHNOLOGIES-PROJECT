#!/usr/bin/env bash
set -o errexit

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Preparing profile images..."
mkdir -p media/bio
cp static/images/profiles/abdul-wahab.jpg media/bio/
cp static/images/profiles/laiba-zainab.jpeg media/bio/

echo "Loading portfolio data from fixture..."
python manage.py loaddata fixtures/portfolio_data.json

echo "Attaching profile images..."
python manage.py shell <<'EOF'
from bio.models import Bio

Bio.objects.filter(slug="abdul-wahab").update(profile_picture="bio/abdul-wahab.jpg")
Bio.objects.filter(slug="laiba-zainab").update(profile_picture="bio/laiba-zainab.jpeg")
EOF

echo "Exporting static site for Netlify..."
python manage.py export_for_netlify

echo "Netlify build complete."
