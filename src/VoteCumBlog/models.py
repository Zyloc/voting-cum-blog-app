from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
# Create your models here.

def upload_location(instance,filename):
	IdeaModel = instance.__class__
	try:
		new_id = IdeaModel.objects.order_by("pk").last().pk + 1		
	except:
		new_id=0
	return "%s/%s" %(new_id, filename)
	#return "%s" %(filename)

'''
	class to store all the contents of Idea(Voting) or Blog

'''
class Idea(models.Model):
	title = models.CharField(max_length=120)
	author = models.CharField(max_length=120)
	cover_image = models.ImageField(upload_to=upload_location,null=True,blank=True)
	content = models.TextField()
	slug = models.SlugField(unique=True,default=None)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	
	def __unicode__(self):
		return self.title
	def __str__(self):
		return self.title	
	class Meta:
		ordering = ["-timestamp","-updated"]
		
	def get_absolute_url(self):
		return reverse("voteCumBlog:detail",kwargs={'pk':self.pk})

def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Idea.objects.filter(slug=slug).order_by("-pk")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().pk)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_idea_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_idea_receiver, sender=Idea)	