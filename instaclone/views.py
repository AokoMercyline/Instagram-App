from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic  import ListView,DetailView, CreateView, UpdateView, DeleteView, View
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.contrib.auth.models import User



class PostListView(ListView):
    # model = Comment
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
   
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context.update({
            'comments': Comment.objects.order_by('created_on'),
            # 'more_context': Model.objects.all(),
        })
        return context

    def get_queryset(self):
        return Post.objects.order_by('-date_posted')
   


class PostDetailView(DetailView):
    model = Post
    

    
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form) 
    
    def test_func(self):
        post = self.get_object() 
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object() 
        if self.request.user == post.author:
            return True
        return False
    
    
def register(request):
    return render(request, 'users/register.html')

def register(request):
    return render(request, 'users/login.html')

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users = User.objects.filter(username__icontains = search_term)
        message = f"{search_term}"
        print(searched_users)
        profile_pic = User.objects.all()
        return render(request, 'instaclone/search.html', {'message':message, 'results':searched_users, 'profile_pic':profile_pic})
    else:
        message = "You haven't searched for any term"
        return render(request, 'instaclone/search.html', {'message':message})

def post_detail(request, slug):
    template_name = 'post_detail.html'
    # post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True) #retrieves all the approved comments from the database.
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
    
def comment(request,post_id):
        current_user=request.user
        post = Post.objects.get(id=post_id)
        profile_owner = User.objects.get(username=current_user.username)
        comments = Comment.objects.all()
        
        if request.method == 'POST':
                form = CommentForm(request.POST, request.FILES)
                if form.is_valid():
                        comment = form.save(commit=False)
                        comment.post = post
                        comment.author = request.user
                        comment.save()
            
                       
                return redirect('instaclone-index')
        else:
                form = CommentForm()
        return render(request, 'instaclone/comment.html',locals())
        
@login_required
def like(request, post_id):
    user = request.user
    post = post.objects.get(id=post_id)
    
    liked = likes.objects.filter(user=user, post=post).count()
    
    if not liked:
        like = likes.objects.Create(user=user, post=post)
        current_likes = current_likes + 1
    else:
        Likes.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1
        
    post.like = current_likes
    post.save()
    
    return HttpResponseRedirect(reverse('MainPage'))

