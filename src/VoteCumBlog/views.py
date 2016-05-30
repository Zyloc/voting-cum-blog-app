from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,DetailView,ListView,UpdateView

from .models import Idea
# Create your views here.

class Home(ListView):
	model = Idea
	template_name = "votecumblog_listView.html"
	paginate_by = "2"
	#context_object_name = "anotherObjectName"
	def get_queryset(self):
		return Idea.objects.all()

class CreatePost(CreateView):
	model = Idea
	fields = ['title','cover_image','content']
	#form_class = IdeaForm
	template_name = "votecumblog_form.html"
	success_url = "/"
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super(CreatePost, self).form_valid(form)

class PostDetail(DetailView):
	model = Idea
	template_name = "votecumblog_detail.html"

class UpdatePost(UpdateView):
	model = Idea
	fields = ["title","cover_image","content"]
	template_name = "votecumblog_form.html"
	success_url = "/"
	def form_valid(self,form):
		form.instance.author = self.request.user 
		return super(CreatePost, self).form_valid(form)



