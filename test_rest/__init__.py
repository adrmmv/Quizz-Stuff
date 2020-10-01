# Import the framework
import os

import markdown

from flask import Flask, g

# Create an instance of flask
from flask_restful import Resource, Api

# Create an instance of Flask
app = Flask(__name__)
# Create the API
api = Api(app)


@app.route("/")
def index():
    """ Present some documentation """

    # Open the readme file
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:
        # read the content
        content = markdown_file.read()
        # Convert to HTML
        return markdown.markdown(content)


class CarlosEsTonto(Resource):
    def get(self):
        return "Correcto siempre lo ha sido!"


api.add_resource(CarlosEsTonto, '/CarlosEsTonto')
