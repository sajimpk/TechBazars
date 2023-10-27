from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login,name="login"),
    path('singup/',singup,name="singup"),
    path('logout/',logout,name="logout"),
    path('forget/',forget,name="forget"),
    path('verify_otp/', verify_otp, name='verify_otp'),
     path('chackout/',chackout_ORDER,name="chackout"),
]