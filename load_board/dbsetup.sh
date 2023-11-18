#!bin/bash
python3 manage.py makemigrations road_data
python3 manage.py sqlmigrate road_data 0001
python3 manage.py migrate