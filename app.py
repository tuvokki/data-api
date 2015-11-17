#!dataapienv/bin/python
from flask import Flask, jsonify
from flask import render_template
from modules.another import AnotherView
from modules.quotes import QuotesView
from modules.squotes import SQuotesView

# app = Flask(__name__)
class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='<%',    # used to be: {%
        block_end_string='%>',      # used to be: %}
        variable_start_string='%%', # used to be: {{
        variable_end_string='%%',   # used to be: }}
        comment_start_string='<#',  # used to be: {#
        comment_end_string='#>',    # used to be: #}
    ))

app = CustomFlask(__name__)

print ("Register QuotesView")
QuotesView.register(app)

print ("Register SQuotesView")
SQuotesView.register(app)

print ("Register AnotherView")
AnotherView.register(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/partials/<path:path>')
def partials(path):
    return render_template('/partials/%s' % path)

@app.route('/<path:path>')
def catch_all(path):
    return 'You want path: %s' % path

# Running with debug on
if __name__ == '__main__':
  app.run(debug=True)
