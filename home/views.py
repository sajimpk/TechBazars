from django.shortcuts import render
from product.models import *
from cart.models import *
# Create your views here.
def home(request):
    cate = category.objects.all()
    prod = product_all.objects.all()
    user =request.user
    if user.is_authenticated:
        crt_list = len(cart.objects.filter(user=user))
        pro = cart.objects.filter(user=user)
        wishlist_list = len(wishlist.objects.filter(user=user))
        total = 0
        for i in pro:
            total += i.product.new_price*i.quantity
    return render(request,'home/home.html',locals())
