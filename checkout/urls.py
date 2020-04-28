from django.conf.urls import url
from .views import checkout, success


urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^success/$', success, name='success'),
]