from django.forms import ModelForm
from django import forms
from gestorFestes.models import Ciutat, Local, Festa

class CiutatForm(ModelForm):

	class Meta:
		model = Ciutat
		exclude = ['user']

class LocalForm(ModelForm):

	class Meta:
		model = Local
		exclude = ['user']

class FestaForm(ModelForm):
	#data = forms.DateTimeField()
	class Meta:
		model = Festa
		exclude = ['user']

