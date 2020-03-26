from django.conf.urls import url, include
from .views import all_products, all_household, all_selfcare, index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^all_products/$', all_products, name='products'),
    url(r'^all_household/$', all_household, name='all_household'),
    url(r'^all_selfcare/$', all_selfcare, name='all_selfcare'),
]