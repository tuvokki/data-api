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

###Usage (behind nginx)
Add the following to your nginx conf:

	upstream quotes_api {
        server 127.0.0.1:5000;
	}
and in the server-section:

        location /quotes/ {
              proxy_redirect off;
              proxy_set_header X-Real-IP $remote_addr;
              proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
              proxy_set_header Host $http_host;
              proxy_set_header X-NginX-Proxy true;

              include uwsgi_params;
              uwsgi_pass quotes_api;
        }
restart the nginx server to make it listen to the correct port and start the flask like this:

`dataapienv/bin/uwsgi --socket 127.0.0.1:5000 -w WSGI:app`

Now the application is available on the following url:

`http://your.host.org/quotes/`

###Todo's:
* Abstract Mongo access
* Config via file or env variables
* Functionality that is actually usefull
