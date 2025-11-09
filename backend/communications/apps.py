# communications/apps.py
from django.apps import AppConfig
import os

class CommunicationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "communications"

    def ready(self):
        # Start scheduler only once (avoid reloading twice during runserver)
        if os.environ.get("RUN_MAIN") == "true" or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
            from . import signals
            from .scheduler import start_scheduler
            start_scheduler()
            print("[communications] Scheduler auto-started with runserver")
        else:
            from . import signals
