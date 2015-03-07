from modules import *

class AnotherView(FlaskView):
  route_base = "home"

  @route('/', methods=['GET', 'POST'])
  @route('/index', methods=['GET', 'POST'])
  def index(self):
    if request.method == "POST":
      return jsonify({'AnotherView': 'index'})
    else:
      return "This is the index of AnotherView"

  @route('/sum/<int:arg1>/<int:arg2>', methods=['POST'])
  def this_view(self, arg1, arg2):
    summedargs = int(arg1) + int(arg2)
    total = "%s + %s = %s" % (arg1, arg2, summedargs)
    result = {
      'arg1': arg1,
      'arg2': arg2,
      'sum': summedargs,
      'total': total
    }
    return jsonify(result)

  def error_call(self):
    bla = "FUBAR"
    # the following line results in an error:
    return "Oh noes, this test goes ", bla
