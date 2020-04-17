from django.conf.urls import url, include
from . import urls_reset
from .views import register, profile, logout, login, order_list

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^order_list/$', order_list, name='order_list'),
    url(r'^password-reset/', include(urls_reset)),
]