# The data API

## Description
The data api is as generic as its name does suspect. You can do all sorts of things with it.

###Prerequisites
A mongo db that is addressable from your application

###Install

    clone https://github.com/tuvokki/data-api.git
    cd data-api
    virtualenv dataapienv
    dataapienv/bin/pip install flask
    dataapienv/bin/pip install flask-classy
    dataapienv/bin/pip install pymongo
    chmod +x app.py

###Usage (in debug mode)
    [ ~/development/projects/data-api]% ]./app.py
	Register QuotesView
	Register AnotherView
    * Running on http://127.0.0.1:5000/
	* Restarting with reloader
	Register QuotesView
	Register AnotherView

###Todo's:
* Abstract Mongo access
* Config via file or env variables
* Functionality that is actually usefull
