from django.apps import AppConfig


class MarketplaceConfig(AppConfig):
    name = 'marketplace'

    def ready(self):
        import os
        import sys
        if 'runserver' not in sys.argv and 'gunicorn' not in sys.argv[0]:
            return
        if os.environ.get('RUN_MAIN', None) != 'true':
            return

        # Pre-warm the RAG engine in a background thread
        import threading
        from assistant.views import _preload_rag
        threading.Thread(target=_preload_rag, daemon=True).start()
