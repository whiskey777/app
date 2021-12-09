from django.urls import path
from django.urls.resolvers import URLPattern
from django.views.generic.base import View
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('metals/', views.getMetals)
]