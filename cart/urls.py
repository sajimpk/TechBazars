from django.urls import path
from .views import *
urlpatterns = [
    path('add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('delete_cart/<int:id>/', delete_crt, name='delete_crt'),
    path('View_crt/', View_crt, name='View_crt'),
    path('crt_up/<int:id>/', crt_up, name='crt_up'),
    path('crt_dw/<int:id>/', crt_dw, name='crt_dw'),
    path('add_wishlist/<int:id>/', add_wishlist, name='add_wishlist'),
    path('View_wishlist/', View_wishlist, name='View_wishlist'),
    path('delete_wishlist/<int:id>/', delete_wishlist, name='delete_wishlist'),
    
]