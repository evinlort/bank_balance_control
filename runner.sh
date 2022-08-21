#!/bin/bash

APP=bank_balance_control
export FLASK_APP=src
export SECRET_KEY='Once there is a way to get back homeward'

source $HOME/$APP/venv/bin/activate
#flask run --host=0.0.0.0 --port=8080
gunicorn -w 4 -b 0.0.0.0:8080 'src:app'
