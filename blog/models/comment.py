from mongoengine import StringField, EmailField, DateTimeField, ListField, EmbeddedDocumentField, ReferenceField
from shared.model.base import MongoBaseModel
from datetime import datetime
from shared.model.tag import Tag




class BlogComment(MongoBaseModel):
    meta = {'collection': 'blog_like'}
    post = ReferenceField('BlogPost', required=True)
    reply_of = ReferenceField('BlogComment', required=False)
    comment = StringField()
    
    