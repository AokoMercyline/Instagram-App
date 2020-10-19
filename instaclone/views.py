from django.shortcuts import render
# from django.http  import HttpResponse
from django.views.generic  import ListView, DetailView, CreateView
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
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
def register(request):
    return render(request, 'users/register.html')

def register(request):
    return render(request, 'users/login.html')


    
