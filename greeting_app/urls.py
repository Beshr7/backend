from django.urls import path
from .views import greeting

urlpatterns = [
    path('greet/', greeting, name='greeting'),
]