from modules import *
from random import choice
from pymongo import MongoClient
from bson.json_util import dumps

class QuotesView(FlaskView):
  # Get a reference to the MongoDB
  client = MongoClient('mongodb://localhost:27017/')
  db = client['quotes']
  collection = db['simple']

  def index(self):
    print ("Getting quotes for you ...")
    quotes = self.db.simple.find()
    # dump the quotes cursor to json
    # return dumps(quotes)
    return jsonify(quotes=dumps(quotes))

  def get(self, quote_id):
    # quote_id = int(quote_id)
    print "This is a test, smile ", quote_id
    document = client.db.collection.find_one({'_id': ObjectId(quote_id)})
    if id < len(self.quotes) - 1:
      return self.quotes[id]
    else:
      return "Not Found", 404

  # The route decorator takes exactly the same parameters as Flask's
  # app.route decorator, so you should feel right at home adding custom
  # routes to any views you create.
  @route('/word_bacon/') #<--- Adding route
  def random(self):
    return choice(self.quotes)
