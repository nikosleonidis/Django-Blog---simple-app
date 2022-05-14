from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'time_create', 'time_update', 'photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_filter = ('time_create',)
    prepopulated_fields = {"title": ("title",)}


admin.site.register(Article, ArticleAdmin)
