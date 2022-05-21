# from django.views.decorators.cache import cache_page
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', ArticleHome.as_view(), name="home"),
    path('create/', CreateArticleView.as_view(), name="create_article"),
    path('article/<int:pk>/', DetailArticleView.as_view(), name="detail_article"),
    path('article/<int:pk>/update',
         EditArticleView.as_view(), name="update_article"),
    path('article/<int:pk>/delete',
         DeleteArticleView.as_view(), name="delete_article"),
]
