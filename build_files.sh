#!/bin/bash

# ติดตั้ง dependencies
python3.12 -m pip install -r requirements.txt

# เก็บ static files
python3.12 manage.py collectstatic --noinput --clear

# รัน migrations (แนะนำให้เพิ่ม)
python3.12 manage.py migrate
