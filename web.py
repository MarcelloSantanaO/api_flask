from flask import Flask
from flask import render_template
from flask_restful import Api
from resources.category_resource import CategoryResource


app = Flask(__name__)

api = Api(app)

api.add_resource(CategoryResource, '/api/category', endpoint='categories')
api.add_resource(CategoryResource, '/api/category/<int:id_>', endpoint='category')


@app.route('/')
def index():
    return render_template('index.html')


app.run(port=5000, host="0.0.0.0")
