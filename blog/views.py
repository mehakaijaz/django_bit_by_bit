from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,DeleteView,DetailView,ListView,UpdateView
)
from .forms import ArticleModelForm
from .models import Article

class ArticleCreateView(CreateView):
    template_name='articles/article_create.html'
    form_class=ArticleModelForm
    queryset=Article.objects.all()#<blog><modelname>list.html
    #success_url='/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
  #  def get_success_url(self):
  #      return '/'

class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()

class ArticleDetailView(ListView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all()
    
    def get_object(self):
        id_=self.kwargs.get('id')
        return get_object_or_404(Article,id)
    
class ArticleUpdateView(ListView):
    template_name = 'articles/article_update.html'
    form_class=ArticleModelForm 
    
    def get_object(self):
        id_=self.kwargs.get('id')
        return get_object_or_404(Article,id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class ArticleDeleteView(ListView):
    template_name = 'articles/article_delete.html'
    #queryset = Article.objects.all()
    def get_object(self):
        id_=self.kwargs.get('id')
        return get_object_or_404(Article,id)
    
    def get_success_url(self):
        return reverse('articles:article-list')