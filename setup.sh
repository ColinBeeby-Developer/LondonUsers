#!/bin/bash

sudo apt-get install libcurl4-openssl-dev libssl-dev
sudo apt install python3-pip
pip3 install pycurl
pip3 install mock==3.0.5
pip3 install geopy
pip3 install flask
pip3 install flask_restplus
pip3 install werkzeug==0.16.1
sudo apt install gunicorn

echo Setup complete!
