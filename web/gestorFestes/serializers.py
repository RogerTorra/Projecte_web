from rest_framework.fields import *
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Local, Festa, Ciutat

class LocalSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='local-detail')
##	festes = HyperlinkedRelatedField(many=True, read_only=True, view_name='festa-detail') ##
	user = CharField(read_only=True)
	class Meta:
		model = Local
		fields = ('url', 'nom', 'descripcio', 'carrer', 'telf', 'email', 'ciutat',
                  'user')
		## fields = ('url', 'nom', 'descripcio', 'carrer', 'telf', 'email', 'ciutat', 'user', 'festes')

class FestaSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='festa-detail')
##	local = HyperlinkedRelatedField(view_name='local-detail') ##
	titol = CharField(read_only=True)
	user = CharField(read_only=True)
##	imatge = ImageField()
##	data = DateTimeField(read_only=True)
	class Meta:
		model = Local
		fields = ('url', 'titol', 'descripcio', 'user')
		## fields = ('url', 'titol', 'descripcio', 'imatge', 'data', 'user', local)

class CiutatSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='ciutat-detail')
    user = CharField(read_only=True)
    class Meta:
        model = Ciutat
        fields = ('url', 'nom', 'provincia', 'cp', 'user')
