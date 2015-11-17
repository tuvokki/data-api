from modules import *
import os
from random import randrange
import sqlite3
from bson.json_util import dumps

class SQuotesView(FlaskView):
  sqlite_file = 'quotes_db.sqlite'
  quotes_table = 'quotes'
  saying_field = 'saying'
  who_field = 'who'
  index_name = 'id'


  def index(self):
    print ("Getting quotes for you ...")
    # Get a reference to the SQLiteDB
    conn = sqlite3.connect(self.sqlite_file)
    c = conn.cursor()
    c.execute('SELECT * FROM {tn}'.\
        format(tn=self.quotes_table))
    quotes = c.fetchall()
    # dump the quotes cursor to json
    result = []
    for quote in quotes:
      result.append({'text': quote[1], 'saying': quote[2], 'id': quote[0]})
    return jsonify(quotes=dumps(result))

  def get(self, quote_id):
    # quote_id = int(quote_id)
    print ("This is a test, smile ", quote_id)
    conn = sqlite3.connect(self.sqlite_file)
    c = conn.cursor()
    c.execute('SELECT * FROM {tn} WHERE {cn}={id}'.\
            format(tn=self.quotes_table, cn=self.index_name, id=quote_id))
    quote = c.fetchone()
    return jsonify(quote=dumps({'text': quote[1], 'saying': quote[2], 'id': quote[0]}))

  # The route decorator takes exactly the same parameters as Flask's
  # app.route decorator, so you should feel right at home adding custom
  # routes to any views you create.
  @route('/word_bacon/') #<--- Adding route
  def random(self):
    print ("Stirring up the frying pan to bake some bacon")
    conn = sqlite3.connect(self.sqlite_file)
    c = conn.cursor()
    c.execute('SELECT * FROM {tn}'.\
        format(tn=self.quotes_table))
    quotes = c.fetchall()
    random_index = randrange(len(quotes))
    quote = quotes[random_index]
    return jsonify(quote=dumps({'text': quote[1], 'saying': quote[2], 'id': quote[0]}))
