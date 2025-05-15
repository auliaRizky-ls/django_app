from django.shortcuts import render, redirect

def products_cart(request):
    cart = request.session.get('cart', [])
    if request.method == 'POST':
        item = request.POST.get('item')
        if item:
            cart.append(item)
            request.session['cart'] = cart
        return redirect('products_cart')
    return render(request, 'hello/index.html', {'cart': cart})

def cart_clear(request):
    request.session.pop('cart', None)
    return redirect('products_cart')
