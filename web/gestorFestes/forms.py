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
	#data = forms.DateTimeField()
	# local = forms.ModelChoiceField(queryset=Local.objects.filter(user=1)) ---> com puk saber kin user sok? 
	class Meta:
		model = Festa
		exclude = ['user']
		# exclude = ['user','local']

