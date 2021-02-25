from flask import Flask
from flask import render_template
from flask_restful import Api
from resourcers.resource_name import Nome


app = Flask(__name__)

api = Api(app)

api.add_resource(Nome, '/api/name')

@app.route('/')
def index():
    return render_template('index.html')

app.run()