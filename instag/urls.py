from django.contrib import admin
from django.urls import include, path
from users import views as user_views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/',LoginView.as_view(), name='Login'),
    path('', include('instaclone.urls')),
]
