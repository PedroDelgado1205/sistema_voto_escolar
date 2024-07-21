from django.urls import path

from .views import inicio_login

urlpatterns = [
    path('', inicio_login, name='inicio_login'),
]
