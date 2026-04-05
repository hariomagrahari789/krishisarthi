from django.apps import AppConfig


import os
import sys

class AiEngineConfig(AppConfig):
    name = 'ai_engine'

    def ready(self):
        # Prevent running during migrations or outer autoreload process
        if 'runserver' not in sys.argv and 'gunicorn' not in sys.argv[0]:
            return
        if os.environ.get('RUN_MAIN', None) != 'true':
            return

        from .views import load_ml_artifacts
        print("📊 [KrishiSaarthi] Django Startup: Preloading Fertilizer recommendation model...")
        load_ml_artifacts()
