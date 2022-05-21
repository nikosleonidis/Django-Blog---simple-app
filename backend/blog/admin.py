from django.contrib import admin
from .models import *

"""
We inform the Django administrator node that our model is registered in the admin panel using a custom
class inherited from ModelAdmin. In this class, you can include information on how to display the model
in the admin panel and how to interact with it. The list_display attribute allows you to specify model
fields that will be displayed on the object list page.
"""


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'author',
                    'photo', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'title': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']


admin.site.register(Article, ArticleAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'article', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')


admin.site.register(Comment, CommentAdmin)
