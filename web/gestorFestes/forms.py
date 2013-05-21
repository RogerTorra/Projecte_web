from django.forms import ModelForm
from gestorFestes.models import Ciutat, Local, Festa

class CiutatForm(ModelForm):
	class Meta:
		model = Ciutat
class LocalForm(ModelForm):
	class Meta:
		model = Local
class FestaForm(ModelForm):
	class Meta:
		model = Festa