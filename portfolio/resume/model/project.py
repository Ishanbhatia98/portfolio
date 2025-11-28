# resume/models_mongo.py
from mongoengine import StringField, EmailField, DateTimeField, ListField, EmbeddedDocumentField, ReferenceField
from shared.model.base import MongoBaseModel
from datetime import datetime
from .line_item import LineItem



class Project(MongoBaseModel):
    meta = {'collection': 'project'}
    name = StringField(required=True, max_length=100)
    published_date = DateTimeField()
    description = ListField(ReferenceField(LineItem), default=[])
    link = StringField(default="")
    #add tags
    def __str__(self):
        return self.name + " - " + self.degree
    