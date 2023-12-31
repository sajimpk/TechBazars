from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth.models import User , auth
import random
from .models import *
from cart.models import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import update_session_auth_hash
import time
# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username = request.POST.get('Username')
        pasword = request.POST.get('password')

        user = auth.authenticate(username=username,password = pasword)
        if user:
            auth.login(request,user)
            return redirect(request.META['HTTP_REFERER'])
        else:
            messages.success(request, "User not found !, Please singup fast")
            return redirect(request.META['HTTP_REFERER'])
 
    return render(request,'account/log_reg.html')



def singup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username = request.POST.get('username')
        pasword = request.POST.get('pass1')
        pasword2 = request.POST.get('pass2')
        fast_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        if pasword:
            a = ['1','2','3','4','5','6','7','8','9','0']
            b = ['@','!','#','%','$','&']
            c = []
            d = []
            for i in a:
                if i in pasword:
                    c.append(i)
            for i in b:
                if i in pasword:
                    d.append(i)
            
            if len(pasword) >= 8:
                if pasword == pasword2:
                    if User.objects.filter(username=username).exists():
                            messages.success(request, "Profile Name Already Taken.")
                    elif User.objects.filter(email=email).exists():
                            messages.success(request, "Profile Email Already Taken. try forget option for new password")
                    else:
                        if len(c) != 0 and len(d) !=0:
                            user = User.objects.create_user(first_name=fast_name, last_name=last_name, email=email,username=username, password=pasword)
                            user.set_password(pasword)
                            user.save()
                            messages.success(request, "Profile Created. You can log in now")
                            return redirect('login')
                            
                        else:
                            messages.success(request, "add a number and spacial charecter on you password")
            else:
                messages.success(request, "Profile pass must be 8 character.")
        
    return render(request,'account/log_reg.html')


def logout(request):
    auth.logout(request)
    return redirect(request.META['HTTP_REFERER'])
 

def forget(request):
    otp = random.randint(0000, 9999)
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            if email:
                send_mail_registration(email, otp)
                user = User.objects.get(email=email)
                if user:
                    try:
                        prof = Profile_otp.objects.get(user=user)
                        if prof:
                            prof.otp = otp
                            prof.save()
                            return redirect('verify_otp')
                    except:
                        prof = Profile_otp.objects.create(user=user, otp=otp)
                        prof.save()
                        return redirect('verify_otp')
        except:
            messages.warning(request, "User Not Found.")
            return redirect('forget')

    return render(request, 'account/forget.html')

def verify_otp(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('pass')
            password1 = request.POST.get('pass1')
            otp = request.POST.get('otp')

            user = User.objects.get(email=email)
            if password==password1:
                if user:
                    prof = Profile_otp.objects.get(user = user)
                    if prof.otp == otp:
                        user.set_password(password)
                        user.save()
                        update_session_auth_hash(request, user)
                        messages.warning(request, "User Password Changed.")
                        return redirect('login')
                    else:
                        messages.warning(request, "Otp not matched Try again.")
                else:
                    messages.warning(request, "User not found ")
            else:
                messages.warning(request, "confrom password not match.")
    except Exception as e :
        messages.warning(request, "User not found")
    return render(request,'account/verify_otp.html',locals())

def send_mail_registration(email, otp):
    subject = "Account Verification otp"
    message = f'hi your verify otp is :  {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

# chack out funtions 

def chackout_ORDER(request):
    user =request.user
    if user.is_authenticated:
        wishlist_list = len(wishlist.objects.filter(user=user))
        crt_list = len(cart.objects.filter(user=user))
        product = cart.objects.filter(user=user)
        
        total = 0
        for i in product:
            total += i.product.new_price*i.quantity
            if i.product.quantity == 0:
                i.quantity=0
                i.save()
        wishlist_show = wishlist.objects.filter(user=user)
    
    return render(request,'account/checkout.html',locals())