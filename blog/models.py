from django.conf import settings
from django.db import models
from django.utils import timezone
from django_extensions.db.fields import AutoSlugField
from django.template.defaultfilters import slugify
from django.urls import reverse

class Tag(models.Model):
	name = models.CharField(max_length=200)
	slug = AutoSlugField(populate_from = 'name')

	def __str__(self):
		return self.name

status = [('Active','Active'),('Inactive', 'Inactive'), ('Drafted', 'Drafted')]

class Category(models.Model):
	title = models.CharField(max_length = 200)
	slug = AutoSlugField(populate_from = 'title')
	content = models.TextField()
	updated_time = models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length = 200, choices = status, default='Active')

	def publish(self):
		self.updated_time = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Post(models.Model):	
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True)
	title = models.CharField(max_length = 200)
	slug = AutoSlugField(populate_from = 'title')
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	# def my_slugify_function(content):
	# 	return content.replace('_', '-').lower()

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return ("/post/%s/" % self.slug)

