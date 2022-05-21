from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseNotFound
from django.views.generic import *
from django.contrib.auth.mixins import *

from .models import *
from .forms import *


# Responsible for the number of items displayed in the 'base.html' file
class DataMixin:
    paginate_by = 8


class ArticleHome(DataMixin, LoginRequiredMixin, ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'home.html'
    ordering = ["-publish"]

    # This function calls the specified name in the title of the browser page
    def get_context_data(self, **kwargs):
        context = super(ArticleHome, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context


class CreateArticleView(DataMixin, LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    context_object_name = 'articles'
    template_name = 'components/create_update_article.html'
    success_url = reverse_lazy('home')
    # login_url = reverse_lazy('home')
    # raise_exception = True

    # This function checks the form for validity
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # This function calls the specified name in the title of the browser page
    def get_context_data(self, **kwargs):
        context = super(CreateArticleView, self).get_context_data(**kwargs)
        context['title'] = 'Добавление новой статьи'
        return context


class DetailArticleView(DataMixin, LoginRequiredMixin, DetailView):
    model = Article
    context_object_name = 'articles'
    template_name = 'components/detail_article.html'

    # This function calls the specified name in the title of the browser page
    def get_context_data(self, **kwargs):
        context = super(DetailArticleView, self).get_context_data(**kwargs)
        context['title'] = 'Подробнее о статье'
        return context


class EditArticleView(DataMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    form_class: ArticleForm
    pk_url_kwarg = 'pk'
    context_object_name = 'articles'
    success_url = reverse_lazy('home')
    template_name = 'components/create_update_article.html'
    fields = ['title', 'body', 'photo', 'title']

    # This function calls the specified name in the title of the browser page
    def get_context_data(self, **kwargs):
        context = super(EditArticleView, self).get_context_data(**kwargs)
        context['title'] = 'Подробнее о статье'
        return context

    # This function checks the form for validity
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # This function is an implementation of the method "EditArticleView"
    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False


class DeleteArticleView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('home')


# We will use the Search Form through which a user will be redirected to the article webpage.
# def SearchView(request):
#    if request.method == 'POST':
#        form = ArticleForm(request.POST)
#
#        if form.is_valid():
#            title = form.cleaned_data['title']
#            return redirect('ArticleHome', title=title)
#
#    else:
#        form = ArticleForm()
#        context = {
#            'form': form,
#        }
#    return render(request, '<home>/Form.html('')', context)


# This function generates a response to the wrong URL 404 (NOT FOUND)
def pageNotFound(exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
