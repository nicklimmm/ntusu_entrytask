from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import PostForm, EditForm
from .models import Post, Category

# def home(request):
#     return render(request, 'home.html')

class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date_posted']

    
    def get_context_data(self, *args,**kwargs):
        categories_menu = Category.objects.all()
        context = super(self.__class__, self).get_context_data(*args, **kwargs)
        context['categories_menu'] = categories_menu
        return context
    


def CategoryView(request, cats):
    categories_menu = Category.objects.all()
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'category.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts, 'categories_menu': categories_menu})


def CategoryList(request):
    categories_menu_list = Category.objects.all()
    return render(request, 'categorylist.html', {'categories_menu_list': categories_menu_list})


class PostDetailed(DetailView):
    model = Post
    template_name = 'postdetailed.html'
    
    def get_context_data(self, *args,**kwargs):
        categories_menu = Category.objects.all()
        context = super(self.__class__, self).get_context_data(*args, **kwargs)
        context['categories_menu'] = categories_menu
        return context


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addpost.html'
    # fields = '__all__'
    # fields = ('title', 'body')

    def get_context_data(self, *args,**kwargs):
        categories_menu = Category.objects.all()
        context = super(self.__class__, self).get_context_data(*args, **kwargs)
        context['categories_menu'] = categories_menu
        return context


class AddCategory(CreateView):
    model = Category
    template_name = 'addcategory.html'
    fields = '__all__'

    def get_context_data(self, *args,**kwargs):
        categories_menu = Category.objects.all()
        context = super(self.__class__, self).get_context_data(*args, **kwargs)
        context['categories_menu'] = categories_menu
        return context


class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'editpost.html'
    # fields = ['title', 'title_tag', 'body']

    def get_context_data(self, *args,**kwargs):
        categories_menu = Category.objects.all()
        context = super(self.__class__, self).get_context_data(*args, **kwargs)
        context['categories_menu'] = categories_menu
        return context


class DeletePost(DeleteView):
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args,**kwargs):
        categories_menu = Category.objects.all()
        context = super(self.__class__, self).get_context_data(*args, **kwargs)
        context['categories_menu'] = categories_menu
        return context


