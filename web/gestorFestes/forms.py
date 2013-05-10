from django.forms import ModelForm
from gestorFestes.models import Ciutat

class CiutatForm(ModelForm):
	class Meta:
		model = Ciutat