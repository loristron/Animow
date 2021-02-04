from django.shortcuts import render, get_object_or_404, redirect, redirect
from .models import Anime
from perfis.models import Perfil
from django.contrib.auth.decorators import login_required
from .forms import ComentarioModelForm
from django.contrib import messages

# Create your views here.
def dynamic_detailed_view(request, slug):
	obj = get_object_or_404(Anime, slug=slug)
	if request.user.is_authenticated: 
		perfil		= Perfil.objects.get(user=request.user)
		assistidos 	= perfil.assistidos.all()
		favoritos 	= perfil.favoritos.all()
		quero_ver 	= perfil.quero_ver.all()

		c_form 		= ComentarioModelForm(request.POST or None)

		if request.POST:
			if c_form.is_valid():
				instance = c_form.save(commit=False)
				instance.autor = perfil
				instance.anime = obj
				instance.save()
				messages.info(request, 'Comentário Enviado!')
				c_form = ComentarioModelForm()

		context 	= {
			'object': obj,
			'page_title': obj.titulo.capitalize(),
			'perfil': perfil,
			'assistidos': assistidos,
			'favoritos': favoritos,
			'quero_ver': quero_ver,
			'c_form'	: c_form,
		}
	else: 
		context 	= {
			'object': obj,
			'page_title': 'Animes Registrados',
		}
	return render(request, 'animes/new_animes_detail.html', context)

def list_animes_view(request):

	queryset 	= Anime.objects.all()
	user 		= request.user

	if user.is_authenticated: 
		perfil		= Perfil.objects.get(user=user)
		assistidos 	= perfil.assistidos.all()
		favoritos 	= perfil.favoritos.all()
		quero_ver 	= perfil.quero_ver.all()
		context 	= {
			'object_list': queryset,
			'page_title': 'Animes Registrados',
			'perfil': perfil,
			'assistidos': assistidos,
			'favoritos': favoritos,
			'quero_ver': quero_ver,
		}
	else: 
		context 	= {
			'object_list': queryset,
			'page_title': 'Animes Registrados',
		}

	return render(request, 'animes/list.html', context)

@login_required
def adicionar_favorito_view(request):
	user 		= request.user
	if request.method == 'POST':
		anime_id 	= request.POST.get('anime_id')
		anime_obj 	= Anime.objects.get(pk=anime_id)
		if user.is_authenticated:
			perfil 	= Perfil.objects.get(user=user)
			perfil.favoritos.add(anime_obj)
			if anime_obj not in perfil.assistidos.all():
				perfil.assistidos.add(anime_obj)
			if anime_obj in perfil.quero_ver.all():
				perfil.quero_ver.remove(anime_obj)
			print("perfil.favoritos: ", perfil.favoritos)

	return redirect(request.META.get('HTTP_REFERER'))

@login_required
def remover_favorito_view(request):
	user 				= request.user
	if request.method 	== 'POST':
		anime_id 		= request.POST.get('anime_id')
		anime_obj 		= Anime.objects.get(pk=anime_id)
		print("anime obj_remove: ", anime_obj)
		if user.is_authenticated:
			perfil 		= Perfil.objects.get(user=user)
			perfil.favoritos.remove(anime_obj)
	return redirect(request.META.get('HTTP_REFERER'))

@login_required
def adicionar_assistido_view(request):
	user 				= request.user
	if request.method == 'POST':
		anime_id 		= request.POST.get('anime_id')
		anime_obj		= Anime.objects.get(pk=anime_id)
		perfil 		= Perfil.objects.get(user=user)
		if anime_obj in perfil.quero_ver.all():
			perfil.quero_ver.remove(anime_obj)
		perfil.assistidos.add(anime_obj)

	return redirect(request.META.get('HTTP_REFERER'))

@login_required
def remover_asistido_view(request):
	user 				= request.user
	if request.method == 'POST':
		if 'remove_asistido' in request.POST:
			anime_id 		= request.POST.get('r_anime_id')
			anime_obj		= Anime.objects.get(pk=anime_id)
			print("anime obj: ", anime_obj)
			if user.is_authenticated:
				perfil 		= Perfil.objects.get(user=user)
				perfil.assistidos.remove(anime_obj)
				print("perfil.assistidos: ", perfil.assistidos)
	return redirect(request.META.get('HTTP_REFERER'))

@login_required
def adicionar_quer_ver_view(request):
	user 				= request.user
	if request.method == 'POST':
		anime_id 		= request.POST.get('anime_id')
		anime_obj 		= Anime.objects.get(pk=anime_id)
		perfil 			= Perfil.objects.get(user=user)

		#LÓGICA PRA QUANDO O ANIME TÁ NA LISTA DE ASSISTIDOS
		if anime_obj in perfil.assistidos.all():
			perfil.assistidos.remove(anime_obj)
		#L´ÓGICA RA QUANDO O ANIME TA NA LISTA DE FAVORITOS
		if anime_obj in perfil.favoritos.all():
			perfil.favoritos.remove(anime_obj)
		#LÓGICA PRA QUANDO O ANIME ASSISTIDO NÃO TÁ NEM NA LISTA DE FAVORITOS NEM NOS ASSISTIDSO
		if anime_obj not in perfil.assistidos.all() and anime_obj not in perfil.favoritos.all():
			perfil.quero_ver.add(anime_obj)
	return redirect(request.META.get('HTTP_REFERER'))










