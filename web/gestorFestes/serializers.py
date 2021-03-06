from rest_framework.fields import *
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Local, Festa, Ciutat

class LocalSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='local-detail')
	user = CharField(read_only=True)
	email = EmailField()
	class Meta:
		model = Local
		fields = ('url', 'nom', 'descripcio', 'carrer', 'telf', 'email', 'ciutat',
                  'user')

class FestaSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='festa-detail')
	titol = CharField()
	user = CharField(read_only=True)
	imatge = FileField()
	data = DateField(format='date' ,input_formats='DD-MM-YYYY')
	class Meta:
		model = Festa
		fields = ('url', 'titol','descripcio','data','imatge','local', 'user')


class CiutatSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='ciutat-detail')
	user = CharField(read_only=True)
	class Meta:
		model = Ciutat
		fields = ('url', 'nom', 'provincia', 'cp', 'user')
