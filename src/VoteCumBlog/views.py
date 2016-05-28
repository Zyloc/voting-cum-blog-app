from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Idea
# Create your views here.

class Home(ListView):
	model = Idea
	template_name = "votecumblog_listView.html"
	paginate_by = "2"
