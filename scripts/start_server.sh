#!/bin/bash

cd /home/ec2-user/flask-app

pkill -f gunicorn || true

nohup gunicorn \
--bind 0.0.0.0:5000 \
app:app \
> app.log 2>&1 &