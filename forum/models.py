from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.urls import reverse
from django import forms


class Category(models.Model):
	CHOICES=(
		('Hospital','Hospital'),
		('College','College'),
		('Hotel','Hotel'),
		('Restaurants','Restaurants'),
		('Movies','Movies'),
		)

	cat=models.CharField(max_length=20,choices=CHOICES)
	imgg=models.ImageField(upload_to='cat_pic', blank=True)

	def __str__(self):
		return self.cat
	def get_absolute_url(self):
		return reverse('identity', kwargs={'pk': self.pk})
	
class Bang(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=50, default='')
	title = models.CharField(max_length=50, default='')
	review = models.TextField(max_length=80, default='')
	rating = models.IntegerField(
			default=1,
			validators = [MaxValueValidator(5), MinValueValidator(1)]
		)
	
	created_at = models.DateTimeField(auto_now_add=True) 
	location = models.CharField(max_length=80, default='')

	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('rev_update', kwargs={'pk': self.pk})
# Create your models here.