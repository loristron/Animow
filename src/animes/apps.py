from django.apps import AppConfig


class AnimesConfig(AppConfig):
    name = 'animes'

    def ready(self):
    	import animes.signals

