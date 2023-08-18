from django.apps import AppConfig
from signals import my_signal

class ProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project'
    def ready(self):
        my_signal.send(sender=self, msg="Сигнал сработал")

