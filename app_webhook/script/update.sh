#!/bin/bash

cd /var/erp
sudo git pull
sudo source venv/bin/activate
sudo python manage.py makemigrations
sudo python manage.py migrate