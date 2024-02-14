from django.apps import AppConfig
from dal.test.utils import fixtures
from django.db.models.signals import post_migrate


class PatientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'patients'

class TestApp(AppConfig):
    name = 'select2_foreign_key'

    def ready(self):
        post_migrate.connect(fixtures, sender=self)

