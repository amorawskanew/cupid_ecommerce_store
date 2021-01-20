from django.shortcuts import render, redirect, reverse, HttpResponse

from products.models import Product

def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})


def add_cart(request, item_id):
    """ Add an item to the cart"""

    cart = request.session.get('cart', {})
    if item_id in cart:
        cart[item_id] = int(cart[item_id])
    else:
        cart[item_id] = cart.get(item_id)
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')    

    request.session['cart'] = cart
    return redirect(reverse('home'))

    
    