from django.urls import path

from .views import (
	dynamic_detailed_view, 
	list_animes_view, 
	adicionar_favorito_view, 
	remover_favorito_view,
	adicionar_assistido_view,
	remover_asistido_view,
	adicionar_quer_ver_view,
	)
from django.conf import settings
from django.conf.urls.static import static

app_name = 'animes'

urlpatterns = [
	path('', list_animes_view, name='lista_animes'),
	path('fav/', adicionar_favorito_view, name='fav-view'),
	path('unfav/', remover_favorito_view, name='unfav-view'),
	path('assistir/', adicionar_assistido_view, name='add-assistido-view'),
	path('unassistir/', remover_asistido_view, name='remove_asistido_view'),
	path('add-querover/', adicionar_quer_ver_view, name='add-quero-ver-view'),
	path('<slug>/', dynamic_detailed_view, name="anime_detalhe"),
	] 

