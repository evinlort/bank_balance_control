#!/bin/bash

DIR=$HOME
#DIR=/opt
APP=bank_balance_control
export DEVELOPMENT=1
export FLASK_APP=src
export SECRET_KEY='Once there is a way to get back homeward'

rm -rf $DIR/$APP/venv
python3 -m pip install virtualenv
python3 -m virtualenv venv

source $DIR/$APP/venv/bin/activate
`which python` -m pip install -r requirements.txt
#flask run --host=0.0.0.0 --port=8080
gunicorn -w 1 -b 0.0.0.0:8080 'src:app'
