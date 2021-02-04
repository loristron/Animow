from django.shortcuts import render, redirect
from .models import  Perfil
from .forms import PerfilModelForm, SocialModelForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages 


# Create your views here.
@login_required
def meu_perfil_view(request):
	template_name = 'perfis/meu-perfil_novo.html'
	user 		= request.user
	obj 		= Perfil.objects.get(user=user)
	form 		= PerfilModelForm(request.POST or None, request.FILES or None, instance=obj)
	social_form = SocialModelForm(request.POST or None, instance=obj)

	if request.method == 'POST':
		print("request: ", request.POST)

		if 'atualiza-info' in request.POST:
			form 	= PerfilModelForm(request.POST or None, request.FILES or None, instance=obj)
			if form.is_valid():
				messages.warning(request, 'Perfil Atualizado')
				form.save()
			return redirect(request.META.get('HTTP_REFERER'))

		if 'atualiza-social' in request.POST:
			if social_form.is_valid():
				messages.warning(request, 'Perfil Atualizado')
				social_form.save()
			return redirect(request.META.get('HTTP_REFERER')) 

	context = {
		'perfil':	obj,
		'page_title': 'Meu Perfil',
		'form'		: form,
		'social_form': social_form,
	}

	return render(request, template_name, context)

@login_required
def meus_assistidos_view(request):
	user 					= request.user
	perfil 					= Perfil.objects.get(user=user)

	favoritos 				= perfil.favoritos.all()
	assistidos 				= perfil.assistidos.all()
	quero_ver				= perfil.quero_ver.all()

	context 				= {
		'object_list': assistidos,
		'page_title': 'Animes Assistidos',
		'perfil': perfil,
		'assistidos': assistidos,
		'favoritos': favoritos,
		'quero_ver': quero_ver,

	}

	template_name 			= 'animes/list.html'
	return render(request, template_name, context)

@login_required
def meus_favoritos_view(request):
	user 					= request.user
	perfil 					= Perfil.objects.get(user=user)

	favoritos 				= perfil.favoritos.all()
	assistidos 				= perfil.assistidos.all()
	quero_ver				= perfil.quero_ver.all()

	context 				= {
		'object_list': favoritos,
		'page_title': 'Animes Favoritos',
		'perfil': perfil,
		'assistidos': assistidos,
		'favoritos': favoritos,
		'quero_ver': quero_ver,

	}

	template_name 			= 'animes/list.html'
	return render(request, template_name, context)

def meus_quero_ver_view(request):
	user 					= request.user
	perfil 					= Perfil.objects.get(user=user)

	favoritos 				= perfil.favoritos.all()
	assistidos 				= perfil.assistidos.all()
	quero_ver				= perfil.quero_ver.all()

	context 				= {
		'object_list': quero_ver,
		'page_title': 'Animes Favoritos',
		'perfil': perfil,
		'assistidos': assistidos,
		'favoritos': favoritos,
		'quero_ver': quero_ver,

	}

	template_name 			= 'animes/list.html'
	return render(request, template_name, context)