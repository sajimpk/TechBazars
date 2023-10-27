from django.urls import path
from .views import *
urlpatterns = [
    path('shop/', shop, name='shop'),
    path('search/', search, name='search'),
    path('category/<int:id>/', product, name='product'),

]