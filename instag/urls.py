from django.contrib import admin
from django.urls import include, url
from users import views as user_views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('register/', user_views.register, name='register'),
    url('', include('blog.urls')),
]
