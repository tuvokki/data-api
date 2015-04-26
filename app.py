#!dataapienv/bin/python
from flask import Flask
from modules.another import AnotherView
from modules.quotes import QuotesView

app = Flask(__name__)

print ("Register QuotesView")
QuotesView.register(app)

print ("Register AnotherView")
AnotherView.register(app)

if __name__ == '__main__':
  app.run(debug=True)
