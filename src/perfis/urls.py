from django.urls import path, include

from .views import (
	meu_perfil_view,
	meus_assistidos_view,
	meus_favoritos_view,
	meus_quero_ver_view,
	)

app_name = 'perfis'

urlpatterns = [
	
	path('meuperfil/', meu_perfil_view, name='user-perfil'),
	path('assistidos/', meus_assistidos_view, name='meus-assistidos-view'),
	path('favoritos/', meus_favoritos_view, name='meus-favoritos-view'),
	path('quero-ver/', meus_quero_ver_view, name='meus-quero-ver'),

]