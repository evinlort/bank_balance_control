#!/bin/bash

#DIR=$HOME
DIR=$HOME/PycharmProjects
APP=bank_balance_control

export DEVELOPMENT=1
export FLASK_APP=src
export SECRET_KEY='Once there is a way to get back homeward'

cd $DIR/$APP
rm -rf $DIR/$APP/venv

python3 -m pip install virtualenv
python3 -m virtualenv $DIR/$APP/venv

source $DIR/$APP/venv/bin/activate
`which python` -m pip install -r $DIR/$APP/requirements.txt
#flask run --host=0.0.0.0 --port=8080

authbind gunicorn -w 1 -b 0.0.0.0:80 "src:app"
