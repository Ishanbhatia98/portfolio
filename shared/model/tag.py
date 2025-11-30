# resume/models_mongo.py
from mongoengine import StringField, EmailField, DateTimeField, ListField, EmbeddedDocumentField, ReferenceField
from shared.model.base import MongoBaseModel
from datetime import datetime




class Tag(MongoBaseModel):
    meta = {'collection': 'tag'}
    name = StringField(required=True, max_length=100, unique=True)

    def __str__(self):
        return self.name 
    