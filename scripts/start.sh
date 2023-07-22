#!/bin/bash

python src/commands/converter.py

exec $(which gunicorn) -c /code/config/gunicorn/config.py src.app:app
