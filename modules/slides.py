from modules import *
import os
from bson.json_util import dumps


class SlidesView(FlaskView):
  def index(self):
      result = []
      for file in os.listdir(os.path.dirname(__file__) + '\..\static\slides\\'):
          result.append({
            'image': '/static/slides/' + file,
            'text': 'Slide'
          })
      return jsonify(slides=result)

