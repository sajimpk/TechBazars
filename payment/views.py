from django.shortcuts import render,redirect
from cart.models import cart
from sslcommerz_lib import SSLCOMMERZ
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def payment(request):
    user = request.user
    if user.is_authenticated:
        all_cart = cart.objects.filter(user=user)
        total = 0
        for i in all_cart:
            subtotal = i.product.new_price * i.quantity
            total += subtotal
    sslcz = SSLCOMMERZ({'store_id': 'niyam6412dc52e1e89', 'store_pass': 'niyam6412dc52e1e89@ssl', 'issandbox': True})
    total_amount = total
    data = {
        'total_amount': total_amount,
        'currency': "BDT",
        'tran_id': "tran_12345",
        'success_url': "http://127.0.0.1:8000/payment/success/",
        'fail_url': "http://127.0.0.1:8000/payment/fail/",
        'emi_option': "0",
        'cus_name': "test",
        'cus_email': "test@test.com",
        'cus_phone': "01700000000",
        'cus_add1': "customer address",
        'cus_city': "Dhaka",
        'cus_country': "Bangladesh",
        'shipping_method': "NO",
        'multi_card_name': "",
        'num_of_item': 1,
        'product_name': "Test",
        'product_category': "Test Category",
        'product_profile': "general",
    }

    response = sslcz.createSession(data)
    return redirect(response['GatewayPageURL'])

@csrf_exempt
def success(request):
    return render (request, 'payment/success.html')

@csrf_exempt
def fail(request):
    return render (request, 'payment/fail.html')