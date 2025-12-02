from rest_framework import serializers
import mongoengine
from bson import ObjectId
from datetime import datetime


class MongoEngineDocumentSerializer(serializers.Serializer):
    """
    Auto-generates DRF serializers from MongoEngine Documents.
    Works with Django 5, DRF 3.14+, Python 3.13.
    """

    document_class = None   # set dynamically

    # ----------------------------------------------------------------------
    # GENERATOR
    # ----------------------------------------------------------------------
    @classmethod
    def build_serializer(cls, document, include_fields=None, exclude_fields=None):
        attrs = {"document_class": document}

        for name, field in document._fields.items():
            if name in ("id", "pk"):
                continue

            if include_fields and name not in include_fields:
                continue
            if exclude_fields and name in exclude_fields:
                continue

            drf_field = cls._convert_mongo_field(field)
            if drf_field:
                attrs[name] = drf_field

        # add id always
        attrs["id"] = serializers.CharField(read_only=True)

        return type(f"{document.__name__}Serializer", (cls,), attrs)

    # ----------------------------------------------------------------------
    # FIELD CONVERSION
    # ----------------------------------------------------------------------
    @staticmethod
    def _convert_mongo_field(field):
        if isinstance(field, mongoengine.StringField):
            return serializers.CharField(required=field.required, allow_null=not field.required)

        if isinstance(field, mongoengine.BooleanField):
            return serializers.BooleanField(required=field.required, allow_null=True)

        if isinstance(field, mongoengine.IntField):
            return serializers.IntegerField(required=field.required, allow_null=True)

        if isinstance(field, mongoengine.DateTimeField):
            return serializers.DateTimeField(required=field.required, allow_null=True)

        if isinstance(field, mongoengine.ListField):
            return serializers.ListField(child=serializers.CharField(), required=False)

        if isinstance(field, mongoengine.ReferenceField):
            # reference stored as ObjectId string (DRF handles str)
            return serializers.CharField(required=False, allow_null=True)

        # fallback
        return serializers.CharField(required=False, allow_null=True)

    # ----------------------------------------------------------------------
    # CREATE
    # ----------------------------------------------------------------------
    def create(self, validated_data):
        model = self.document_class
        obj = model()

        for field_name, value in validated_data.items():
            value = self._convert_value_for_mongo(obj, field_name, value)
            setattr(obj, field_name, value)

        obj.save()
        return obj

    # ----------------------------------------------------------------------
    # UPDATE
    # ----------------------------------------------------------------------
    def update(self, instance, validated_data):
        for field_name, value in validated_data.items():
            value = self._convert_value_for_mongo(instance, field_name, value)
            setattr(instance, field_name, value)

        instance.save()
        return instance

    # ----------------------------------------------------------------------
    # HELPER: Convert DRF input → MongoEngine-compatible value
    # ----------------------------------------------------------------------
    def _convert_value_for_mongo(self, instance, field_name, value):
        field = instance._fields.get(field_name)

        # ReferenceField → convert string ID → Document
        if isinstance(field, mongoengine.ReferenceField):
            if value in (None, ""):
                return None
            try:
                return field.document_type.objects(id=ObjectId(value)).first()
            except Exception:
                return None

        # ListField of ReferenceFields or strings
        if isinstance(field, mongoengine.ListField):
            if value is None:
                return []
            if not isinstance(value, list):
                # if user sends comma-separated string
                value = [v.strip() for v in str(value).split(",") if v.strip()]

            # Handle ReferenceField inside ListField
            if isinstance(field.field, mongoengine.ReferenceField):
                converted = []
                for item in value:
                    try:
                        doc = field.field.document_type.objects(id=ObjectId(item)).first()
                        if doc:
                            converted.append(doc)
                    except Exception:
                        pass
                return converted

            return value

        # DateTimeField: convert str → datetime
        if isinstance(field, mongoengine.DateTimeField):
            if isinstance(value, str):
                try:
                    return datetime.fromisoformat(value)
                except Exception:
                    return None
            return value

        # Primitive fields
        return value