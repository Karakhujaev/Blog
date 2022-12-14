# Import Post class from articles/models.py.
from re import template
from statistics import mode
from .models import Post

# Automate open the given page
from django.urls import reverse_lazy

# LoginRequiredMixin for control to display pages.
from django.contrib.auth.mixins import LoginRequiredMixin

# UserPassesTestMixin for control to update posts and compare user with owner of the post after allow to update or delete. 
from django.contrib.auth.mixins import UserPassesTestMixin

# Import Django Views.
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Views.
class AboutPageView(TemplateView):
    """ About Page View """
    template_name = 'pages/about.html'

class PostListView(ListView):
    """ Home Page View """
    model = Post
    template_name = 'pages/home.html'

class AiListView(ListView):
    """ Home Page View """
    model = Post
    template_name = 'pages/ai.html'

class CryptoListView(ListView):
    """ Home Page View """
    model = Post
    template_name = 'pages/crypto.html'

class SoftwareListView(ListView):
    """ Home Page View """
    model = Post
    template_name = 'pages/software.html'

class TechListView(ListView):
    """ Home Page View """
    model = Post
    template_name = 'pages/tech.html'

class PostDetailView(DetailView):
    """ Post Page View """
    model = Post
    template_name = 'pages/post_detail.html'

class ControlListView(LoginRequiredMixin, ListView):
    """ Control Page View """
    model = Post
    template_name = 'control.html'

class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """ Create Post View """
    model = Post
    template_name = 'post_new.html'
    fields = ['category',  'title',  'summary', 'image',  'body', ]

    def test_func(self):
        return self.request.user.is_superuser

class PostUpdateView(LoginRequiredMixin, UpdateView):
    """ Update Post View """
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'category', 'summary', 'image', 'body']

class PostDeleteView(LoginRequiredMixin, DeleteView):
    """ Delete Post View """
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('control')

    """ Compare user with owner of the post """
    # def test_func(self):
    #     obj = self.get_object()
    #     return obj.author == self.request.user

class PostcontrolDetailView(LoginRequiredMixin, DetailView):
    """ Control Post Detail View """
    model = Post
    template_name = 'post_control_detail.html'

