#!/bin/bash

rm db.sqlite3
rm -rf ./knifeapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations knifeapi
python3 manage.py migrate knifeapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

