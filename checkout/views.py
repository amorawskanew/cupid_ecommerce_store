from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.conf import settings 
from django.core.mail import send_mail 
from  django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.shortcuts import  reverse
from django.contrib import messages



from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe


  
from django.shortcuts import render, redirect, reverse
from django.contrib import messages




def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_0SMREd7Vdweb1MGRi8S0EycR00JVzSAs5O',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

# Create your views here.


#add Checkout Function
@login_required
def checkout(request):
    if request.method == 'POST':
        return redirect('stripe_payment')
    else:
        return render(request, 'checkout/checkout.html')

# add stripe function
@login_required
def stripeOpen(request):
    
    if request.method == 'POST':
        get_order = {
                "order_number" : "123456",
                "full_name":"anna",
                "date": "22/01/2021",
                "order_total":"order_total",
                "delivery_cost":"delivery_cost",
                "grand_total":"grand_total",
                "street_address1":"street_address1",
                "town_or_city":"town_or_city",
                "country":"country",
                
            }
            
        body = render_to_string('confirmation_emails/email_body.html',{
            'order' : get_order,
            'contact_email' : 'contact_email'
        })
        email_subject = render_to_string('confirmation_emails/email_subject.html', {
            'order_number':get_order.get('order_number')
        })
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [request.POST.get('stripeEmail'), ] 
        send_mail(subject=email_subject, message=body, from_email=email_from, recipient_list=recipient_list ) 
        request.session['cart'] = {}
        return redirect('home')
    else:
        return render(request, 'checkout/stripePayment.html')
