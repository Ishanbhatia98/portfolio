# resume/apps.py
from django.apps import AppConfig

class ResumeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'resume'

    def ready(self):
        from portfolio.mongo import connect_db
        connect_db()