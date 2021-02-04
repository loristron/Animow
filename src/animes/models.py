


from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from .utils import get_random_code

#from perfis.models import Perfil
#from perfis.models import Perfil

# Create your models here.

AGE_CHOICES = (
	('L', 'L'),
	('10', '10'),
	('12', '12'),
	('14', '14'),
	('16', '16'),
	('18', '18'),

	)


class Anime(models.Model):

	titulo 			= models.CharField(max_length=300)
	titulo_original = models.CharField(max_length=300, null=True, blank=True)
	sinopse 		= models.TextField()
	nota_imdb		= models.DecimalField(default=0, blank=True, max_digits=2, decimal_places=1)
	capa 			= models.ImageField(upload_to='media/capas')

	c_indicativa	= models.CharField(choices=AGE_CHOICES, max_length=25, blank=True)
	tempo_medio_ep	= models.IntegerField(default=0, blank=True)
	num_toal_ep		= models.IntegerField(default=0, blank=True)
	num_temporadas 	= models.IntegerField(default=0, blank=True)
	num_ep_temporada= models.IntegerField(default=0, blank=True)

	ano_inicio		= models.IntegerField(default=0, blank=True)
	ano_termino 	= models.IntegerField(default=0, blank=True)

	categorias 		= models.CharField(max_length=500, blank=True)
	autor 			= models.CharField(max_length=100, blank=True)

	assistido_por	= models.ManyToManyField(to='perfis.Perfil', blank=True, related_name='usuarios_assistiram')
	favorito_por	= models.ManyToManyField(to='perfis.Perfil', blank=True, related_name='usuarios_favoritaram')
	querem_ver		= models.ManyToManyField(to='perfis.Perfil', blank=True, related_name='usuarios_querem_ver')

	slug 			= models.SlugField(blank=True)


	def __str__(self):
		return self.titulo

	def get_num_assistidos(self):
		return self.assistido_por.all().count()
	def get_num_favoritos(self):
		return self.favorito_por.all().count()
	def get_num_querem_ver(self):
		return self.querem_ver.all().count()

	def get_comentarios(self):
		return self.comentario_set.all()
	def get_num_comentarios(self):
		return self.comentario_set.all().count()
		
	def get_absolute_url(self):
		return reverse('animes:anime_detalhe', kwargs={"slug": self.slug})

	def save(self, *args, **kwargs):
		to_slug 		= slugify(str(self.titulo))
		if Anime.objects.filter(slug=to_slug).exists():
			to_slug = slugify(to_slug + '-' + str(get_random_code()))
		self.slug 		= to_slug
		super().save(*args, **kwargs)


class Comentario(models.Model):
	autor 		= models.ForeignKey(to='perfis.Perfil', on_delete=models.CASCADE)
	anime 		= models.ForeignKey(Anime, on_delete=models.CASCADE)
	conteudo	= models.TextField(max_length=300)
	data 		= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.autor.user}-{self.anime}-{self.pk}" 
