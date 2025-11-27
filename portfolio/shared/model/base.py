

# created at , updated at 
# created by
# deleted at, is deleted
# deleted by
# resume/models_mongo.py
from mongoengine import Document, StringField, EmailField, DateTimeField
from datetime import datetime



class MongoBaseModel(Document):
    meta = {'abstract': True}
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
    created_by = StringField()
    updated_by = StringField()
    deleted_at = DateTimeField()
    is_deleted = StringField()
    deleted_by = StringField()


    def save(self, *args, **kwargs):
        self.updated_at = datetime.utcnow()
        return super(MongoBaseModel, self).save(*args, **kwargs)
    
    def soft_delete(self, deleted_by=None):
        self.is_deleted = True
        self.deleted_at = datetime.utcnow()
        self.deleted_by = deleted_by
        self.save()