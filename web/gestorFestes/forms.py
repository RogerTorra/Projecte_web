from django.forms import ModelForm
from django import forms
from gestorFestes.models import Ciutat, Local, Festa
from django.contrib.auth.models import User

class CiutatForm(ModelForm):

	class Meta:
		model = Ciutat
		exclude = ['user']

class LocalForm(ModelForm):
	
	class Meta:
		model = Local
		exclude = ['user']

class FestaForm(ModelForm):

# Activan aquesta funcio nomes et mostra els locals que ha creat l'usuari, pero llavors no carrega la imatge
#	def __init__(self, *args, **kwargs):
#		locals_user = kwargs.pop('locals_user', None)
#		super(FestaForm, self).__init__(*args, **kwargs)
#		self.fields['local'] = forms.ModelChoiceField(locals_user)
		

	class Meta:
		model = Festa
		exclude = ['user']

