from django.shortcuts import render
# from django.http  import HttpResponse
from django.views.generic  import ListView
from .models import Post

# Create your views here.
def index(request):
    context = {
        'posts': Post.objects.all()
    }
   
    return render(request, 'index.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'

def register(request):
    return render(request, 'users/register.html')

def register(request):
    return render(request, 'users/login.html')



