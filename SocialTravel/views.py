from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView, DeleteView
from SocialTravel.models import Post
from django.urls import reverse_lazy

def index(request):
    return render(request,"SocialTravel/index.html")

class PostList(ListView):
    model = Post
    #Post.objects.all() se utiliza la query para buscar lista   

class PostDetail(DetailView):
    model = Post
    #Post.objects.get(id=pk)

class PostCreate(CreateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = '__all__' #o si quiere usarse algunos campos , se usa lista con los nombres de los campos 
    # ['carousel_caption_tittle','carousel_caption_description']

class PostUpdate(UpdateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = '__all__'

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy("post-list")
    