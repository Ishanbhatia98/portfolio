# resume/models_mongo.py
from mongoengine import StringField, EmailField, DateTimeField, ListField, EmbeddedDocumentField, ReferenceField, Document
from datetime import datetime


class User(Document):
    meta = {'collection': 'user'}
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
    
    first_name = StringField(required=False, max_length=100)
    last_name = StringField(required=False, max_length=100)
    full_name = StringField(required=False, max_length=200)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    profile_picture = StringField()

    linkedin_url = StringField()
    github_url = StringField()
    leetcode_url = StringField()
    website_url = StringField()

    codechef_url = StringField()
    hackerrank_url = StringField()
    codeforces_url = StringField()

    summary = StringField()
    





    def __str__(self):
        return self.name 
    
    def save(self):
        if not self.full_name:
            self.full_name = f"{self.first_name} {self.last_name}"
        return super().save()



    