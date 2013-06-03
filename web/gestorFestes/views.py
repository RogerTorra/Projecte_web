# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from gestorFestes.models import Festa,Ciutat,Local,LocalReview
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import get_object_or_404

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


# Forms #

from forms import CiutatForm, LocalForm, FestaForm
from  django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy

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

class CiutatUpdate(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
	model = Ciutat
	template_name = 'form.html'
	form_class = CiutatForm

class CiutatDelete(LoginRequiredMixin, CheckIsOwnerMixin,DeleteView):
	model = Ciutat
	success_url = reverse_lazy('ciutat_lis')

class LocalCreate(LoginRequiredMixin , CreateView):
	model = Local
	template_name = 'form.html'
	form_class = LocalForm
	def form_valid(self,form):
		form.instance.user = self.request.user
		return super(LocalCreate,self).form_valid(form)

class LocalUpdate(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
	model = Local
	template_name = 'form.html'
	form_class = LocalForm

class LocalDelete(LoginRequiredMixin, CheckIsOwnerMixin,DeleteView):
	model = Local
	success_url = reverse_lazy('local_lis')

class FestaCreate(LoginRequiredMixin , CreateView):
	
	model = Festa
	template_name = 'form.html'
	form_class = FestaForm

#	def get_form(self, form_class):
#		return form_class(
#			locals_user=Local.objects.filter(user=self.request.user.id)
#	)

	def form_valid(self,form):
		form.instance.user = self.request.user
		return super(FestaCreate,self).form_valid(form)

class FestaUpdate(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
	model = Festa
	template_name = 'form.html'
	form_class = FestaForm

class FestaDelete(LoginRequiredMixin, CheckIsOwnerMixin,DeleteView):
	model = Festa
	success_url = reverse_lazy('festa_lis')

@login_required()
def review(request, pk):
	local = get_object_or_404(Local, pk=pk)
	review = LocalReview(rating=request.POST['rating'],
		comment=request.POST['comment'],
		user=request.user,
		local=local)
	review.save()
	return HttpResponseRedirect(urlresolvers.reverse('local_detail', args=(local.id,)))



# RESTful API #

from rest_framework import generics, permissions
from serializers import LocalSerializer, FestaSerializer, CiutatSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		return obj.user == request.user

class APILocalList(generics.ListCreateAPIView):
	permission_classes = (IsOwnerOrReadOnly,)
	model = Local
	serializer_class = LocalSerializer

class APILocalDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsOwnerOrReadOnly,)
	model = Local
	serializer_class = LocalSerializer

class APIFestaList(generics.ListCreateAPIView):
	permission_classes = (IsOwnerOrReadOnly,)
	model = Festa
	serializer_class = FestaSerializer

class APIFestaDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsOwnerOrReadOnly,)
	model = Festa
	serializer_class = FestaSerializer

class APICiutatList(generics.ListCreateAPIView):
	permission_classes = (IsOwnerOrReadOnly,)
	model = Ciutat
	serializer_class = CiutatSerializer

class APICiutatDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsOwnerOrReadOnly,)
	model = Ciutat
	serializer_class = CiutatSerializer
