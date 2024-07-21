from django.urls import path

from .views import candidatos

urlpatterns = [
    path('', candidatos, name='candidatos'),
]