import sys
sys.path.append('.')

from models.model_base import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import validates


class CategoryModel(BaseModel):
    __tablename__ = 'categories_category'

    name = Column('name', String(length=50), nullable=False)
    description = Column('description', String(length=255))


    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @validates('name')
    def validates_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not name.strip():
            raise ValueError("Name can't be empty.")
        if len(name) > 50:
            raise ValueError("Name must be smaller than 50 char")
        return name

    @validates('description')
    def validates_description(self, key, description):
        if not isinstance(description, str):
            raise TypeError("Description must be a string.")
        if len(description) > 255:
            raise ValueError("Description must be smaller than 255 char.")
        return description
