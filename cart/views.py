from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.
def add_to_cart(request, id):
    prod = product_all.objects.get(id=id)
    user = request.user
    if user.is_authenticated:
        try:
            
            pro = cart.objects.filter(product=prod,user=user)
            if pro:
                for i in pro:
                    i.quantity += 1
                    i.save()
                    return redirect(request.META['HTTP_REFERER'])
            else:
                crt = cart.objects.create(
                    user=user,
                    product=prod
                )
                crt.save()
                return redirect(request.META['HTTP_REFERER'])
        except Exception as e:
            print(e)
    else:
        messages.warning(request, "Please Login or Register Fast")
        return redirect('login')
    
def delete_crt(request, id):
    pro = cart.objects.get(id=id)
    pro.delete()
    return redirect(request.META['HTTP_REFERER'])

def View_crt(request):
    user =request.user
    if user.is_authenticated:
        crt_list = len(cart.objects.filter(user=user))
        pro = cart.objects.filter(user=user)
        total = 0
        for i in pro:
            total += i.product.new_price*i.quantity
            if i.product.quantity == 0:
                i.quantity=0
                i.save()
    return render(request,'cart/cart.html',locals())




def crt_up(request, id):
    prod = product_all.objects.get(id=id)
    user = request.user
    if user.is_authenticated:
        pro = cart.objects.filter(product=prod,user=user)
        pro.quantity+=1
        pro.save()
        return redirect("home")
def crt_dw(request, id):
    prod = product_all.objects.get(id=id)
    user = request.user
    if user.is_authenticated:
        pro = cart.objects.filter(product=prod,user=user)
        pro.quantity-=1
        pro.save()
        return redirect("home")
        
        
# start wishlist from heare
def add_wishlist(request, id):
    prod = product_all.objects.get(id=id)
    user = request.user
    if user.is_authenticated:
        try:
            pro = wishlist.objects.filter(product=prod,user=user)
            if pro:
                messages.warning(request, "alredy added ")
                return redirect(request.META['HTTP_REFERER'])
            else:
                crt = wishlist.objects.create(
                    user=user,
                    product=prod
                )
                crt.save()
                return redirect(request.META['HTTP_REFERER'])
        except Exception as e:
            print(e)
    else:
        messages.warning(request, "Please Login or Register Fast")
        return redirect('login')
    
def View_wishlist(request):
    user =request.user
    if user.is_authenticated:
        wishlist_list = len(wishlist.objects.filter(user=user))
        crt_list = len(cart.objects.filter(user=user))
        product = cart.objects.filter(user=user)
        total = 0
        for i in product:
            total += i.product.new_price*i.quantity
        wishlist_show = wishlist.objects.filter(user=user)
    else:
        messages.warning(request, "Please Login or Register Fast")
        return redirect('login')
    return render(request,'cart/wishlist.html',locals())

def delete_wishlist(request, id):
    pro = wishlist.objects.get(id=id)
    pro.delete()
    return redirect(request.META['HTTP_REFERER'])