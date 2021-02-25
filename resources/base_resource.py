from flask_restful import Resource
from flask import request


class BaseResource(Resource):
    def __init__(self, dao, model_type):
        self.__dao = dao
        self.__model_type = model_type

    def get(self, id_ = None):
        if id_:
            return self.__dao.read_by_id(id_)
        return self.__dao.read_all()

    def post(self):
        json = request.json
        model = self.__model_type(**json)
        self.__dao.save(model)
        return model, 201

    def put(self, id_):
        json = request.json
        model = self.__dao.read_by_id(id_)

        for key, value in json.items():
            setattr(model, key, value)
        self.__dao.save(model)
        return model, 200

    def delete(self, id_):
        model = self.__dao.read_by_id(id_)
        self.__dao.delete(model)
        return None, 204
