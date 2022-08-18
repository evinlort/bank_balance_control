#!/bin/bash

export FLASK_APP=src
export SECRET_KEY='Once there is a way to get back homeward'

flask run --host=0.0.0.0 --port=8080
