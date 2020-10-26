from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import PostForm, EditForm
from .models import Post

# def home(request):
#     return render(request, 'home.html')

class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date_posted']


class PostDetailed(DetailView):
    model = Post
    template_name = 'postdetailed.html'


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'addpost.html'
    # fields = '__all__'
    # fields = ('title', 'body')


class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'editpost.html'
    # fields = ['title', 'title_tag', 'body']


class DeletePost(DeleteView):
    model = Post
    template_name = 'deletepost.html'
    success_url = reverse_lazy('home')



# def loginuser(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('posts')
#     context = {}
#     return render(request, 'login.html', context)

# def registeruser(request):
#     form = CreateUserForm()

#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request, 'Account was created for ' + user)
#             return redirect('login')

#     context = {'form': form}
#     return render(request, 'register.html', context)