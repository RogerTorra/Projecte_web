# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from gestorFestes.models import Festa,Ciutat,Local
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect

def festes(request): 
	try:
		festes = Festa.objects.all()
	except:
		raise Http404('Festes not found')
	variables = Context({
		'festes': festes,	
        'titlehead': 'Gestor de Festes',
		'pagetitle': 'Festes',
	})

	return render(request,"festes.html",variables)

def festa_info(request,idFesta):
	try:
		festa = Festa.objects.get(pk=idFesta)
	except:
		raise Http404('Festa not found')
	variables = Context({
		'festa': festa,	
        'titlehead': 'Nom de la festa',
		'pagetitle': 'Nom de la festa',
	})
	return render(request,"festa.html",variables)


def index(request): 
	
	variables = Context({
        'titlehead': 'Gestor de Festes',
		'pagetitle': 'Gestor de Festes',
		'contentbody': "Informant de tota la festa d'arreu desde 2013",
		'nomUsuari' : obtenirUsuari(request),
	})
	
	
	return render(request,"index.html",variables)

def obtenirUsuari(request):

	if(request.user.is_authenticated()):
		return request.user.username
	else:
		return "Anonim"

def logout_view(request):
    logout(request)
    # Redirect to a success page.


def ciutats(request): 
	try:
		ciutats = Ciutat.objects.all()
	except Exception:
		raise Http404('Ciutats not found.')
	
	variables = Context({
		'ciutats': ciutats,	
        'titlehead': 'Gestor de Festes',
		'pagetitle': 'Llistat de Ciutats',
	})

	return render(request,"ciutats.html",variables)

def ciutat_info(request,idCiutat):
	try:
		ciutat = Ciutat.objects.get(pk=idCiutat)
	except Exception:
		raise Http404('Ciutat not found.')
	
	variables = Context({
		'ciutat': ciutat,	
        'titlehead': 'Gestor de Festes',
		'pagetitle': ciutat.nom,
	})

	return render(request,"ciutat.html",variables)

def locals_view(request): 
	try:
		locals_obj = Local.objects.all()
	except Exception:
		raise Http404('Ciutats not found.')
	
	variables = Context({
		'locals': locals_obj,	
        'titlehead': 'Gestor de Festes',
		'pagetitle': 'Llistat de Locals',
	})

	return render(request,"locals.html",variables)

def locals_info(request,idLocal): 
	try:
		local = Local.objects.get(pk=idLocal)
		festes = Festa.objects.filter(local=idLocal)
	except Exception:
		raise Http404('Ciutats not found.')
	
	variables = Context({
		'local': local,	
        'titlehead': 'Gestor de Festes',
		'pagetitle': local.nom,
		'festes' : festes,
	})

	return render(request,"local.html",variables)

def locals_ciutat(request,idCiutat): 
	try:
		local = Local.objects.filter(ciutat=idCiutat)
		ciutat = Ciutat.objects.get(pk=idCiutat)
	except Exception:
		raise Http404('Ciutats not found.')
	
	variables = Context({
		'local': local,	
        'titlehead': 'Gestor de Festes',
		'pagetitle': 'Locals de '+ciutat.nom,
		'locals' : local,
	})

	return render(request,"locals.html",variables)


def festes_local(request,idLocal):
	try:
		local = Local.objects.get(pk=idLocal)
		festes = Festa.objects.filter(local=idLocal)
	except Exception:
		raise Http404('Ciutats not found.')
	
	variables = Context({	
        'titlehead': 'Gestor de Festes',
		'pagetitle': local.nom,
		'festes' : festes,
		'local' : idLocal,
	})

	return render(request,"festesLocal.html",variables)



def festa_info_json(request,idFesta):
	try:
		data = Festa.objects.get(pk=idFesta)
		from django.core import serializers
		festa = serializers.serialize("json", data)

	except:
		raise Http404('Festa not found')
	#self.response.out.write(simplejson.dumps(festa))
	#variables = Context({
	#	'festa': festa,	
    #    'titlehead': 'Nom de la festa',
	#	'pagetitle': 'Nom de la festa',
	#})
	#return render(request,"festa.html",variables)

#Forms
from forms import CiutatForm
from  django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied

class LoginRequiredMixin(object):

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
	def get_object(self, *args, **kwargs):
		obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
		if not obj.user == self.request.user:
			raise PermissionDenied
		return obj

class CiutatCreate(LoginRequiredMixin , CreateView):
	model = Ciutat
	template_name = 'form.html'
	form_class = CiutatForm
	def form_valid(self,form):
		form.instance.user = self.request.user
		return super(CiutatCreate,self).form_valid(form)
		# if not request.user.is_authenticated():
		# Do something for authenticated users.
		#	return super(CiutatCreate,self).form_valid(form)