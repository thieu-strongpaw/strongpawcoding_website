from django.contrib import admin
from spblog.models import Blog

class BlogAdmin(admin.ModelAdmin):
    pass

admin.site.register(Blog, BlogAdmin)
