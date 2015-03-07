from modules import *
from random import choice

class QuotesView(FlaskView):
  # we'll make a list to hold some quotes for our app
  quotes = [
    "A noble spirit embiggens the smallest man! ~ Jebediah Springfield",
    "If there is a way to do it better... find it. ~ Thomas Edison",
    "No one knows what he can do till he tries. ~ Publilius Syrus"
  ]

  def index(self):
    return "<br>".join(self.quotes)

  def get(self, id):
    id = int(id)
    print "This is a test, smile ", id
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
