# support rich text
# recently release tag

from mongoengine import StringField, EmailField, DateTimeField, ListField, EmbeddedDocumentField, ReferenceField, IntField, BooleanField
from shared.model.base import MongoBaseModel
from datetime import datetime
from shared.model.tag import Tag
from .like import BlogLike
from .comment import BlogComment




class BlogPost(MongoBaseModel):
    meta = {'collection': 'blog_post'}

    is_published = BooleanField(default=False)
    published_at = DateTimeField(default=datetime.utcnow)   
    title = StringField(required=True, max_length=100, unique=True)

    
    summary = StringField(required=True, max_length=300) # generate using gpt
    content = StringField(required=True)


    tags = ListField(ReferenceField(Tag), default=[])
    likes = ListField(ReferenceField(BlogLike), default=[])
    comments = ListField(ReferenceField(BlogComment), default=[])
    time_to_read = IntField(required=False, default=0)


    def __str__(self):
        return self.title 
    
    def save(self, *args, **kwargs):
        if self.is_published and not self.published_at:
            self.published_at = datetime.utcnow()
        if self.deleted_at!=None:
            self.is_published = False
            self.published_at = None
        
        if not self.summary:
            self.summary = self.content[:297] + '...' if len(self.content) > 300 else self.content
        return super(BlogPost, self).save(*args, **kwargs)
    