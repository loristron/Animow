




from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from .utils import get_random_code
from animes.models import Anime, Comentario

import uuid as u

# Create your models here.
class Perfil(models.Model):
	primeiro_nome	= models.CharField(max_length=50)
	sobrenome		= models.CharField(max_length=50)
	email			= models.EmailField(max_length=200)
	user 			= models.OneToOneField(User, on_delete=models.CASCADE)
	avatar			= models.ImageField(default='avatar.png', upload_to='profiles-pics')
	
	country			= models.CharField(max_length=50, blank=True)
	city			= models.CharField(max_length=50, blank=True)

	twitter			= models.CharField(max_length=300, blank=True, null=True)
	instagram		= models.CharField(max_length=300, blank=True, null=True)
	github			= models.CharField(max_length=300, blank=True, null=True)
	facebook		= models.CharField(max_length=300, blank=True, null=True)

	
	favoritos		= models.ManyToManyField(to='animes.Anime', blank=True, related_name='favoritos')
	assistidos		= models.ManyToManyField(to='animes.Anime', blank=True, related_name='assistidos')
	quero_ver		= models.ManyToManyField(to='animes.Anime', blank=True, related_name='quero_ver')
	
	slug			= models.SlugField(unique=True, blank=True)


	def get_favoritos(self):
		return self.favoritos.all()
	def get_num_favoritos(self):
		return self.favoritos.all().count()

	def get_assistidos(self):
		return self.assistidos.all()
	def get_num_assistidos(self):
		return self.assistidos.all().count()

	def get_quero_ver(self):
		return self.quero_ver.all()
	def get_num_quero_ver(self):
		return self.quero_ver.all().count()




	def __str__(self):
		return f"{self.user.username}"

	def save(self, *args, **kwargs):
		if not self.slug:
			aux = False
			if self.primeiro_nome and self.sobrenome:
				perfil_slug 	= slugify(str(self.primeiro_nome) + ' ' + str(self.sobrenome))
				aux				= Perfil.objects.filter(slug=perfil_slug).exists()
				while aux:
					perfil_slug = slugify(perfil_slug + '-' + str(get_random_code()))
			else:
				perfil_slug		= str(self.user)
			self.slug 			= perfil_slug
			super().save(*args, **kwargs)
		else:
			super().save(*args, **kwargs)