
# resume/models_mongo.py
from mongoengine import StringField, EmailField, DateTimeField, ListField, IntField
from shared.model.base import MongoBaseModel
from datetime import datetime
from .line_item import LineItem


class Skill(LineItem):
    meta = {'collection': 'skill'}
    proficiency = IntField(min_value=1, max_value=10, default=1)

    def __str__(self):
        return self.name 
    