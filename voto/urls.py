from django.urls import path
from . import views

urlpatterns = [
    path('', views.votar, name='votar'),
]
