from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,DetailView,ListView

from .models import Idea
# Create your views here.

class Home(ListView):
	model = Idea
	template_name = "votecumblog_listView.html"
	paginate_by = "2"
	# def get_queryset(self):
	# 	return Idea.objects.all()

class CreatePost(CreateView):
	model = Idea
	fields = ['title','content']
	template_name = "votecumblog_form.html"
	success_url = "/"
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super(CreatePost, self).form_valid(form)

class PostDetail(DetailView):
	model = Idea
	template_name = "votecumblog_detail.html"
