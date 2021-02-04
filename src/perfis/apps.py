from django.apps import AppConfig


class PerfisConfig(AppConfig):
    name = 'perfis'

    def ready(self):
    	import perfis.signals