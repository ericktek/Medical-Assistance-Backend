from django.apps import AppConfig


class MainAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Main_app'

    # def ready(self):
        # from .Validators import updater
        # updater.start()
