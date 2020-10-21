from django.urls import path
from django.conf.urls import url
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views


urlpatterns = [
    url(r'$', PostListView.as_view(), name='instaclone-index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    # path('post/<int:pk>/comment/', PostCommentView.as_view(), name='post-comment'),
    path('post/search/', views.search_results,  name='username'),
    path('<slug:slug>/', views.post_detail, name='post_detail')

]      
