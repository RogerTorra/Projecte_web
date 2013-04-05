#encoding:utf-8
from django.db import models

# Create your models here.

class Festa(models.Model):
	titol = models.CharField(max_length=25, unique=True)
	descripcio = models.TextField(max_length=200)
	imatge = models.ImageField(upload_to='imatgesFesta', verbose_name='Imatge')
	data = models.DateTimeField()


class Local(models.Model):
	nom = models.CharField(max_length=25, unique=True)
	descripcio = models.TextField(max_length=200)
	carrer = models.TextField(max_length=50)
	telf = models.IntegerField(verbose_name='Telefon')
	email = models.EmailField(verbose_name='Email de contacte', max_length="30")
	

class Ciutat(models.Model):
	nom = models.CharField(max_length=25, unique=True)
	provincia = models.CharField(max_length=25)
	cp = models.IntegerField(verbose_name='Codi Postal')
	