#!dataapienv/bin/python
from flask import Flask, jsonify
from modules.another import AnotherView
from modules.quotes import QuotesView
from modules.sqllitequotes import SQLLiteQuotesView

app = Flask(__name__)

print ("Register QuotesView")
QuotesView.register(app)

print ("Register SQLLiteQuotesView")
SQLLiteQuotesView.register(app)

print ("Register AnotherView")
AnotherView.register(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'You want path: %s' % path

# Running with debug on
if __name__ == '__main__':
  app.run(debug=True)
