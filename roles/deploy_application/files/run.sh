#!/bin/bash

export INSTANCE_PATH="/opt/example/instance"
exec /opt/example/venv/bin/gunicorn -b 0.0.0.0:5000 wsgi:app

