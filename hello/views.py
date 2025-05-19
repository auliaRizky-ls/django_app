from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

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

#question 9-1 list all items
def item_list(request):
    items = Item.objects.all()
    return render(request, 'hello/item_list.html', {'items': items})

#question 9-2 liss only item with price == 100
def items_price_100(request):
    items = Item.objects.filter(price=100)
    return render(request, 'hello/item_list.html', {'items': items})

#question 10 item management
def manage_item(request):
    items = Item.objects.all()
    if request.method == 'POST':
        if 'delete_id' in request.POST:
            Item.objects.filter(id=request.POST['delete_id']).delete()
        else:
            form = ItemForm(request.POST)
            if form.is_valid():
                form.save()
        return redirect('manage_items')
    else:
        form = ItemForm()
    return render(request, 'hello/item_list_add_edit.html', {'items': items, 'form': form})