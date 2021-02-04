from django.db.models.signals import post_save, m2m_changed
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Perfil
from animes.models import Anime

@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
	print('sinal enviado de User para o Perfil')
	if created:
		Perfil.objects.create(user=instance, primeiro_nome=str(instance.first_name).capitalize(), sobrenome=str(instance.last_name).capitalize(), email=instance.email)