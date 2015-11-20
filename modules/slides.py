from modules import *
import os
# from bson.json_util import dumps


class SlidesView(FlaskView):

    def index(self):
        result = []
        our_path = os.path.dirname(__file__)
        dir_path = os.path.join(our_path, "..", "static", "slides")
        for file in os.listdir(dir_path):
            result.append({
                'image': '/static/slides/' + file,
                'text': 'slide'
            })
        return jsonify(slides=result)
