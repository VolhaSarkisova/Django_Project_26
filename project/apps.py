from django.apps import AppConfig


class ProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project'

    def ready(self):
        import project.signals
        project.signals.my_signal.send(sender=self, msg="Сигнал сработал")

