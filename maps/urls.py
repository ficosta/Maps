from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'bing/', views.bing, name="bing"),
    url(r'/', views.default_map, name="default"),
]
