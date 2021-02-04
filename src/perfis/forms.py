from django import forms
from .models import Perfil

class PerfilModelForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = [
			'primeiro_nome',
			'sobrenome',
			'avatar',
			'country',
			'city',
		]
class SocialModelForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = [
			'twitter',
			'instagram',
			'github',
			'facebook',

		]