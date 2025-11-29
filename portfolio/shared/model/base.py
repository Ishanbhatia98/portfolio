

# created at , updated at 
# created by
# deleted at, is deleted
# deleted by
# resume/models_mongo.py
from mongoengine import Document, StringField, EmailField, DateTimeField, ReferenceField
from datetime import datetime
from uauth.model.user import User



class MongoBaseModel(Document):
    meta = {'abstract': True}
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
    created_by = ReferenceField(User)
    updated_by = ReferenceField(User)
    deleted_at = DateTimeField()
    deleted_by = ReferenceField(User)


    def save(self, *args, **kwargs):
        self.updated_at = datetime.utcnow()
        if args and isinstance(args[0],  User):
            self.created_by = self.created_by or args[0]
            self.updated_by = args[0]
        return super(MongoBaseModel, self).save(*args, **kwargs)
    
    def soft_delete(self, deleted_by=None):
        self.is_deleted = True
        self.deleted_at = datetime.utcnow()
        self.deleted_by = deleted_by
        self.save()