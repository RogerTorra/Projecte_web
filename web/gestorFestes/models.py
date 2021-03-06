#encoding:utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import models as auth_models
from django.contrib.auth.management import create_superuser
from django.db.models import signals
from django.conf import settings
from datetime import date

# Prevent interactive question about wanting a superuser created.  (This code
# has to go in this otherwise empty "models" module so that it gets processed by
# the "syncdb" command during database creation.)
signals.post_syncdb.disconnect(
    create_superuser,
    sender=auth_models,
    dispatch_uid='django.contrib.auth.management.create_superuser')


# Create our own test user automatically.

def create_testuser(app, created_models, verbosity, **kwargs):
  if not settings.DEBUG:
    return
  try:
    auth_models.User.objects.get(username='admin')
  except auth_models.User.DoesNotExist:
    print '*' * 80
    print 'Creating Admin user -- login: admin, password: admin'
    print '*' * 80
    assert auth_models.User.objects.create_superuser('admin', 'x@x.com', 'admin')
  else:
    print 'Test user already exists.'

signals.post_syncdb.connect(create_testuser,
    sender=auth_models, dispatch_uid='common.models.create_testuser')

# Create your models here.

class Ciutat(models.Model):
	provincia = models.CharField(max_length=25)
	nom = models.CharField(max_length=25, unique=True, verbose_name="Ciutat")
	cp = models.IntegerField(verbose_name='Codi Postal')
	user = models.ForeignKey(User, blank=False)
	def __unicode__(self):
		return self.nom
	def get_absolute_url(self):
		return reverse('ciutat_detail', kwargs={'idCiutat': self.id})

class Local(models.Model):
	nom = models.CharField(max_length=25, unique=True)
	descripcio = models.TextField(max_length=200)
	carrer = models.TextField(max_length=50)
	telf = models.IntegerField(verbose_name='Telefon')
	email = models.EmailField(verbose_name='Email de contacte', max_length="30")
	ciutat = models.ForeignKey(Ciutat)
	user = models.ForeignKey(User, blank=False)
	def __unicode__(self):
		return self.nom
	def get_absolute_url(self):
		return reverse('local_detail', kwargs={'idLocal': self.id})


class Festa(models.Model):
	titol = models.CharField(max_length=25, unique=True)
	descripcio = models.TextField(max_length=200)
	imatge = models.ImageField(upload_to='imatgesFesta', verbose_name='Imatge', null = True, blank= True)
	data = models.DateField()
	local = models.ForeignKey(Local)
	user = models.ForeignKey(User, blank=False)
	def __unicode__(self):
		return self.titol
	def get_absolute_url(self):
		return reverse('festa_detail', kwargs={'idFesta': self.id})

class Review(models.Model):
	RATING_CHOICES = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
	rating = models.PositiveSmallIntegerField('Ratings (stars)', blank=False, default=3, choices=RATING_CHOICES)
	comment = models.TextField(blank=True, null=True)
	user = models.ForeignKey(User, blank=False)
	date = models.DateField(default=date.today)

	#class Meta:
	#	abstract = True

class LocalReview(Review):
	local = models.ForeignKey(Local)

