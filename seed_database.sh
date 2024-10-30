#!/bin/bash

# Remove the database and migrations
rm db.sqlite3
rm -rf ./knifeapi/migrations

# Make initial migrations for all installed apps
python3 manage.py migrate

# Create new migrations for knifeapi app
python3 manage.py makemigrations knifeapi

# Apply migrations for knifeapi
python3 manage.py migrate

# Load all necessary fixture data in the correct order
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata bladetypes
python3 manage.py loaddata mods
python3 manage.py loaddata knives
python3 manage.py loaddata knifemods
