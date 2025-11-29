# resume/models_mongo.py
from mongoengine import StringField, EmailField, DateTimeField
from shared.model.base import MongoBaseModel
from datetime import datetime



class ContactMessage(MongoBaseModel):
    meta = {'collection': 'contact_message'}
    name = StringField(required=True, max_length=100)
    email = EmailField()
    number = StringField()
    message = StringField()
    created_at = DateTimeField(default=datetime.utcnow)