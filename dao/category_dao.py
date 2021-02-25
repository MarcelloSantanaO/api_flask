import sys
sys.path.append('.')

from dao.base_dao import BaseDao
from models.category_model import CategoryModel


class CategoryDao(BaseDao):
    def __init__(self):
        super().__init__(CategoryModel)
