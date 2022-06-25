from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import Post

class PostListView(ListView):
    model = Post

class PostCreatView(CreateView):
    model = Post
    fields - "__all__"
    sucess_url = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog")


