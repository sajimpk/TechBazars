from django.urls import path
from .views import *
urlpatterns = [
    path('payment', payment, name='payment'),
    path('success/', success, name='success'),
    path('fail/', fail, name='fail'),
]