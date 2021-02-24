from flask_restful import Resource


class Nome(Resource):
    def get(self):
        return {'name':'Marcello'}
