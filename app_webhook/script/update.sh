#!/bin/bash

cd /var/erp
git pull
source venv/bin/activate
python manage.py migrate