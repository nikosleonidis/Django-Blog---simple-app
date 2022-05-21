#from taggit.managers import TaggableManager
from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# This is our basic model for blog entries (blog articles)
class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовать'),
    )
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    #slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField(max_length=500, verbose_name="Текст статьи")
    photo = models.ImageField(
        blank=True, upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата публикации статьи")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Дата редактирования статьи")
    author = models.ForeignKey(
        User, related_name='blog_articles', default='', on_delete=models.CASCADE, verbose_name="Имя автора")
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='published', verbose_name="Статус")
    #tags = TaggableManager()

    class Meta:
        ordering = ["-publish"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', kwargs={'article.pk': self.pk})


# This is our Comment model. It contains ForeignKey to link a comment to a specific post
class Comment(models.Model):
    article = models.ForeignKey(
        Article, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    #email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Комментарий {} на {}'.format(self.name, self.article)
