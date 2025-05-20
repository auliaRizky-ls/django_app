from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
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

#question 10-2 edit item
def item_edit_list(request):
    items = Item.objects.all()
    return render(request, 'hello/item_edit_list.html', {'items': items})

def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_edit_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'hello/edit_item.html', {'form': form,'item': item})

#question 11-1 search item by name
def search_item_by_name(request):
    q = request.GET.get('q', '')
    result = Item.objects.filter(name__icontains=q) if q else []
    return render(request, 'hello/search_item_by_name.html', {'results': result, 'q': q})

#question 11-2 search item by price
def search_item_by_price(request):
    q = request.GET.get('q', '')
    try:
        price = float(q) if q else 0
        result = Item.objects.filter(price=price) if q else []
    except ValueError:
        result = []
    return render(request, 'hello/search_item_by_price.html', {'results': result, 'q': q})

# Reference: docs/django_exercise.md
# Question 12-1 create a function to sort the items by price (ascending and descending)
def sort_items_by_price(request):
    order = request.GET.get('order', 'asc')
    items = Item.objects.all().order_by('price' if order == 'asc' else '-price')
    return render(request, 'hello/sorted_item_by_price.html', {'items': items})