from django.urls import path
from . import views

urlpatterns = [
    path('', views.item2, name = 'about'),
]