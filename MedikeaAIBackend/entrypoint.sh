#!/bin/sh

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py insert_data

python manage.py spectacular --file schema.yml 

python3 manage.py runserver 0.0.0.0:8000
