from __future__ import unicode_literals

from django.db import models

# Create your models here.
'''
	class to store all the contents of Idea(Voting) or Blog

'''
class Idea(models.Model):
	title = models.CharField(max_length=120)
	author = models.CharField(max_length=120)
	#cover_image = models.ImageField(null=True,blank=True)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

