from django.conf.urls import url     
from .views import blog, create_blog

urlpatterns = [
    url(r'^$', blog, name='blog'),
    url(r'^create/$', create_blog, name='create_blog'),
]