from django.views.decorators.cache import cache_page
from django.urls import path
from .views import *
#    cache_page(60) - Value 60 - the number of seconds to store data in the cache
urlpatterns = [
    path('', ArticleHome.as_view(), name="home"),
    path('create/', cache_page(60)(CreateArticleView.as_view()), name="create-article"),
    path('article/<int:pk>/', DetailArticleView.as_view(), name="detail-article"),
    path('article/<int:pk>/update', EditArticleView.as_view(), name="update-article"),
    path('article/<int:pk>/delete', DeleteArticleView.as_view(), name="delete-article"),
]
