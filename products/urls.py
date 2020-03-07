from django.conf.urls import url, include
from .views import all_products, all_household

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^all_household/$', all_household, name='all_household'),
]