from django.shortcuts import render
from product.models import *
from cart.models import *
# Create your views here.
def product(request,id):
    cate = category.objects.all()
    cat = category.objects.get(id=id)
    prod = product_all.objects.filter(category=cat)
    user =request.user
    if user.is_authenticated:
        crt_list = len(cart.objects.filter(user=user))
        product_total = cart.objects.filter(user=user)
        total = 0
        for i in product_total:
            total += i.product.new_price*i.quantity
    return render(request,'product/product.html',locals())

def shop(request):
    cate = category.objects.all()
    prod = product_all.objects.all()
    user =request.user
    if user.is_authenticated:
        crt_list = len(cart.objects.filter(user=user))
        wishlist_list = len(wishlist.objects.filter(user=user))
        pro = cart.objects.filter(user=user)
        total = 0
        for i in pro:
            total += i.product.new_price*i.quantity
    return render(request,'product/shop.html',locals())



def search(request):
    cate = category.objects.all()
    if request.method == 'GET':
        src = request.GET.get('search')
        print(src)
        if src:
            prod = product_all.objects.filter(name__icontains=src)
        elif src==None:
            prod = product_all.objects.all()
        else:
            prod = product_all.objects.all()
    return render(request,'product/shop.html',locals())