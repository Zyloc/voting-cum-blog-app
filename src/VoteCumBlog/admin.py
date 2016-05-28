from django.contrib import admin

# Register your models here.
from .models import Idea

class IdeaModelAdmin(admin.ModelAdmin):
	list_display = ["title","timestamp","updated"]
	class Meta:
		model = Idea


admin.site.register(Idea,IdeaModelAdmin)		