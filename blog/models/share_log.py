# support rich text
# recently release tag

# resume/models_mongo.py
from mongoengine import StringField, EmailField, DateTimeField, ListField, EmbeddedDocumentField, ReferenceField
from shared.model.base import MongoBaseModel
from datetime import datetime
from shared.model.tag import Tag




class PostShareLog(MongoBaseModel):
    meta = {'collection': 'post_share_log'}
    
    def __str__(self):
        return self.name 
    