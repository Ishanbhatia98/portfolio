# resume/models_mongo.py
from mongoengine import StringField, EmailField, DateTimeField, ListField, EmbeddedDocumentField, ReferenceField
from shared.model.base import MongoBaseModel
from datetime import datetime
from .line_item import LineItem



class WorkExperience(MongoBaseModel):
    meta = {'collection': 'work_experience'}
    org = StringField(required=True, max_length=100)
    role = StringField(default="")
    start_date = DateTimeField()
    end_date = DateTimeField()
    description = ListField(ReferenceField(LineItem), default=[])
    location = StringField(default="")

    
    def __str__(self):
        return self.name + " - " + self.degree
    