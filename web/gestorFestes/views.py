# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from gestorFestes.models import Festa,Ciutat,Local
from django.shortcuts import render

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

def index(request): 
	variables = Context({
        'titlehead': 'Gestor de Festes',
		'pagetitle': 'Gestor de Festes',
		'contentbody': "Informant de tota la festa d'arreu desde 2013",
	})

	return render(request,"index.html",variables)

def userpage(request, username):
	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('User not found.')
	festes = Festa.objects.all()
	variables = Context({
	'username': username,
	'festes': festes,
	})
	
	return render(request, "userpage.html", variables)

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


