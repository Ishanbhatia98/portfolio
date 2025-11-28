# resume/models_mongo.py
from mongoengine import StringField, EmailField, DateTimeField, ListField, EmbeddedDocumentField, ReferenceField
from shared.model.base import MongoBaseModel
from datetime import datetime
from resume.model.line_item import LineItem



class Certificate(MongoBaseModel):
    meta = {'collection': 'certificate'}
    title = StringField(required=True, max_length=100)
    issuer = StringField(default="")
    date = DateTimeField()
    description = ListField(ReferenceField(LineItem), default=[])
    link = StringField(default="")

    def __str__(self):
        return self.name 
    