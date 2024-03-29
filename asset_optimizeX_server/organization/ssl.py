import string
import random
from django.contrib.auth.decorators import login_required  
from sslcommerz_lib import SSLCOMMERZ
from .models import PaymentGateWaySettings
import os
from dotenv import load_dotenv
load_dotenv()

def unique_transaction_id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@login_required 
def sslcommerz_payment_gateway(request, order_id,org_id, name, user_id, amount):
    gateway_auth_details = PaymentGateWaySettings.objects.all().first()
    
    settings = {'store_id': gateway_auth_details.store_id,
                'store_pass': gateway_auth_details.store_pass, 'issandbox': True}

 
    sslcommez = SSLCOMMERZ(settings)
    post_body = {}
    post_body['total_amount'] = amount
    post_body['currency'] = "BDT"
    post_body['tran_id'] = unique_transaction_id_generator()
    lnk = os.getenv("BACKEND_URL")
    post_body['success_url'] = f'{lnk}api/organization/success/'
    post_body['fail_url'] = f'{lnk}orders/payment/faild/'
    post_body['cancel_url'] = f'{lnk}'
    post_body['emi_option'] = 0
    post_body['cus_name'] = name
    post_body['cus_email'] = 'request.user.email'  # Retrieve email from the current user session
    post_body['cus_phone'] = 'request.user.phone'  # Retrieve phone from the current user session
    post_body['cus_add1'] = 'Nothing'  # Retrieve address from the current user session
    post_body['cus_city'] = 'nothing'  # Retrieve city from the current user session
    post_body['cus_country'] = 'Bangladesh'
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "request.user.name"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"

    # OPTIONAL PARAMETERS
    post_body['value_a'] = order_id
    post_body['value_b'] = user_id
    post_body['value_c'] = org_id
    post_body['value_d'] = amount

    response = sslcommez.createSession(post_body)
    print(response)
    # return JsonResponse(response)
    return 'https://sandbox.sslcommerz.com/gwprocess/v4/gw.php?Q=pay&SESSIONKEY=' + response["sessionkey"]