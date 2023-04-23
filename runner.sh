#!/bin/bash

#DIR=$HOME
export -p | grep DIR > /dev/null
if [ $(echo $?) -eq 0 ]
then
  echo "DIR";
else
  exit 1
fi
APP=bank_balance_control

export DEVELOPMENT=1
export FLASK_APP=src
export SECRET_KEY='Once there is a way to get back homeward'
export -p | grep DATABASE > /dev/null
if [ $(echo $?) -eq 0 ]
then
  echo "$DATABASE";
else
  exit 1
fi
#export DATABASE='bbc'

cd "$DIR"/$APP || exit
rm -rf "$DIR"/$APP/venv

python3 -m pip install virtualenv
# shellcheck disable=SC2086
python3 -m virtualenv $DIR/$APP/venv

# shellcheck disable=SC1090
source "$DIR"/$APP/venv/bin/activate
$(which python) -m pip install -r "$DIR"/$APP/requirements.txt
#flask run --host=0.0.0.0 --port=8080

#authbind gunicorn -w 1 -b 0.0.0.0:80 "src:app"
authbind gunicorn -w 1 -b 0.0.0.0:8080 "src:app"
