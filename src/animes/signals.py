


from django.db.models.signals import m2m_changed, post_save, pre_delete
from django.dispatch import receiver

from .models import Anime
from perfis.models import Perfil

@receiver(m2m_changed, sender=Perfil.assistidos.through)
def updade_anime_assistido_por(sender, instance, action, **kwargs):
	
	
	if action == 'post_add' or action == 'pre_add':
		for a in instance.assistidos.all():
			obj = Anime.objects.get(titulo=a)
			obj.assistido_por.add(instance)
	
	if action == 'post_remove' or action == 'pre_remove':
		aux = Anime.objects.all()
		for a in instance.assistidos.all():
			other = aux.exclude(titulo=a)
		for b in other:
			b.assistido_por.remove(instance)

@receiver(m2m_changed, sender=Perfil.favoritos.through)
def update_anime_favoritos_por(sender, instance, action, **kwargs):
	print('favorito action: ', action)

	if  action == 'post_add':
		for a in instance.favoritos.all():
			# if not instance.assistidos.filter(titulo=a).exists(): 
			# 	aux = Anime.objects.get(titulo=a)
			# 	instance.assistidos.add(aux)
			obj = Anime.objects.get(titulo=a)
			obj.favorito_por.add(instance)

	if action == 'post_remove' or action == "pre_remove":

		aux 	= Anime.objects.all()
		ins 	= True
		for a in instance.favoritos.all():
			other = aux.exclude(titulo=a)
		for b in other:
			b.favorito_por.remove(instance)


@receiver(m2m_changed, sender=Perfil.quero_ver.through)
def update_quero_ver(sender, instance, action, **kwargs):
	print ('quero ver action: ', action)
	if action == 'post_add':
		for a in instance.quero_ver.all():
			if instance.assistidos.filter(titulo=a).exists() or instance.favoritos.filter(titulo=a).exists():
				instance.assistidos.remove(a) #não deveria salvar
			else:
				obj = Anime.objects.get(titulo=a)
				obj.querem_ver.add(instance)

	if action == 'post_remove':
		aux = Anime.objects.all()
		for a in instance.quero_ver.all():
			other = aux.exclude(titulo=a)
		for b in other:
			b.querem_ver.remove(instance)
			


