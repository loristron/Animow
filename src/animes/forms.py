

from django import forms 
from .models import Comentario

class ComentarioModelForm(forms.ModelForm):
	conteudo = forms.CharField(label='', 
						widget=forms.TextInput(attrs={
							'placeholder': 'Escrever comentário',

							})
			)
	class Meta:
		model =  Comentario
		fields = [
			'conteudo',
		]