#!bin/bash
python manage.py makemigrations road_data
python manage.py sqlmigrate road_data 0001
python manage.py migrate