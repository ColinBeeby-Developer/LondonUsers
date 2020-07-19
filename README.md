# DWP Technical Test Solution

## Overview

This API uses a Swagger client to access bpdts-app API. This solution uses Flask to expose an API which has a single endpoint. When called this single endpoint will return a list of users who are living in London or whose coordinates are within 50 miles of London. This API has been written in python (3.8.2)

This solution has been deployed as a Heroku app. [Click here](https://londoners.herokuapp.com) to visit the Heroku app.

## Dependencies

* flask
* flask-restplus
* geopy
* gunicorn
* mock
* requests
* werkzeug


## Getting Started

To get the software for dwp-test, please run the following

```
git clone https://github.com/ColinBeeby-Developer/dwp-test
```

Now run the script to set up the required packages

```
cd dwp-test
./setup.sh
```

### Running dwp-test locally

You will need to have python3 set up as your default python instance in order to run this code.

```
gunicorn londonersapi:app
```

To view the Swagger documentation, browse to this location

```
http://127.0.0.1:8000
```

To call the API

```
curl -X GET http://localhost:8000/users/london
```

## Running the tests

To run the automated unit tests which are included with this solution, in the dwp-test folder run the following commands.

```
python -m unittest discover -k unit_test -v
```

To run the automated integration tests which are included with this solution, in the dwp-test folder run the following commands.

On one instance of the command line 

```
gunicorn londonersapi:app
```
On another instance of the command line

```
python -m unittest discover -k integration_test -v
```
