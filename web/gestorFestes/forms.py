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
	#local = forms.ModelChoiceField(queryset=Local.objects.filter(user=1)) 

	#local = forms.ModelChoiceField()

	
#	def __init__(self, *args, **kwargs):
#		self.user = kwargs.pop('user', None)
		#self.validate = kwargs.pop('validate', False)
#		super(FestaForm, self).__init__(*args, **kwargs)
		#self.fields['local'].queryset = Local.objects.filter(user=self.user)
		#user_id = User.objects.get(username = self.user)
		
		#self.fields['local'] = forms.ModelChoiceField(queryset=Local.objects.filter(user=user_id.id))

	class Meta:
		model = Festa
		exclude = ['user']
		#fields = ['titol', 'descripcio', 'imatge', 'data', 'local', 'user']
		#exclude = ['user','local']

