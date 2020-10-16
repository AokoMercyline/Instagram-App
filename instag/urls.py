from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url('', include('instaclone.urls')),
    url(r'^admin/', admin.site.urls),
]
