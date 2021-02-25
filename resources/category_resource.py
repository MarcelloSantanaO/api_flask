from flask_restful import marshal_with, fields
from resources.base_resource import BaseResource
from models.category_model import CategoryModel
from dao.category_dao import CategoryDao


class CategoryResource(BaseResource):
    fields = {
        "id_": fields.Integer,
        "name": fields.String,
        "description": fields.String,
    }

    def __init__(self):
        self.__dao = CategoryDao()
        self.__model_type = CategoryModel
        super().__init__(self.__dao, self.__model_type)

    @marshal_with(fields)
    def get(self, id_ = None):
        return super().get(id_)

    @marshal_with(fields)
    def post(self):
        return super().post()

    @marshal_with(fields)
    def put(self, id_):
        return super().put(id_)

    @marshal_with(fields)
    def delete(self, id_):
        return super().delete(id_)
