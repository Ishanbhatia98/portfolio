# resume/models_mongo.py
from mongoengine import StringField, EmailField, DateTimeField, ListField, EmbeddedDocumentField, EmbeddedDocument
from shared.model.base import MongoBaseModel
from datetime import datetime


class LinkItem(EmbeddedDocument):
    name = StringField(required=True, max_length=100)
    url = StringField(required=True)

class LineItem(MongoBaseModel):
    meta = {'collection': 'line_item', 'allow_inheritance': True}
    name = StringField(required=True, max_length=100)
    description = StringField(default="")
    link = ListField(EmbeddedDocumentField(LinkItem), default=[])

    def __str__(self):
        return self.name
    
    @classmethod
    def create(cls, name:str, description:str="", link:list=[]):
        line_item = cls(
            name=name,
            description=description,
            link=[
                LinkItem(name=item['name'], url=item['url']) for item in link
            ]
        )
        line_item.save()
        return line_item

    def update(self, name:str=None, description:str=None, link:list=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if link is not None:
            self.link = [
                LinkItem(name=item['name'], url=item['url']) for item in link
            ]
        self.save()
        return self
    

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "description": self.description,
            "link": [
                {"name": item.name, "url": item.url} for item in self.link
            ]
        }

