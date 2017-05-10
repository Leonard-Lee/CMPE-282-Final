#!/bin/bash
export MYDIR=/Users/leonardlee/PycharmProjects/CMPE_282_FINAL/src

# install the libraries for Python Web App
pip install flask
pip install PyMySQL
pip install pymongo

echo 'DEBUG: start directory'
echo $(pwd)

cd $MYDIR
export FLASK_APP=app.py
export FLASK_DEBUG=1

# run flask
echo 'DEBUG: end directory'
echo $(pwd)
flask run --host=0.0.0.0 --port=8000
