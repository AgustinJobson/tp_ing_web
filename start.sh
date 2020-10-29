#!/bin/sh

python tpingweb/manage.py migrate
python tpingweb/manage.py runserver 0.0.0.0:8000