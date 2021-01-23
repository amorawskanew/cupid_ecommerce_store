from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.conf import settings 
from django.core.mail import send_mail 
from  django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

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
                "phone_number":"phone_number",
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



    def checkout_success(request, order_number):
    
        """Handle successful checkouts"""

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
