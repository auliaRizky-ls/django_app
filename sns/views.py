from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Message, Good
from .forms import PostForm

# index view
@login_required(login_url='/admin/login/')
def index(request, page=1):
    max = 10 # max number of messages per page
    form = PostForm(request.user)
    msgs = Message.objects.all()
    paginator = Paginator(msgs, max) # create a paginator object
    page_items = paginator.get_page(page) # get the current page items

    params = {
        'login_user': request.user,
        'form': form,
        'contents': page_items,  # Changed from 'content' to 'contents'
    }
    return render(request, 'sns/index.html', params)

# goods view
@login_required(login_url='/admin/login/')
def goods(request):
    goods = Good.objects.filter(owner=request.user).all()

    params = {
        'login_user': request.user,
        'contents': goods,  # Changed from 'content' to 'contents'
    }
    return render(request, 'sns/good.html', params)

# message post view
@login_required(login_url='/admin/login/')
def post(request):
    # POST transmission process
    if request.method == 'POST':
        content = request.POST.get('content')
        # create message, set, and save
        msg = Message()
        msg.owner = request.user
        msg.content = content
        msg.save()
        return redirect(to='/sns/')
    else:
        messages = Message.objects.filter(owner=request.user).all()
        params = {
            'login_user': request.user,
            'contents': messages,  # Changed from 'content' to 'contents'
        }
        return render(request, 'sns/post.html', params)

# good button process
@login_required(login_url='/admin/login/')
def good(request, good_id):
    # fetch the messages that has good
    good_msg = Message.objects.get(id=good_id)

    # count how many times the user has already given good
    is_good = Good.objects.filter(owner=request.user).filter(message=good_msg).count()

    # if greater than 0, the user has already given good
    if is_good > 0:
        messages.success(request, 'You have already given good to this message.')
        return redirect(to='/sns/')
    
    # good count on message +1
    good_msg.good_count += 1
    good_msg.save()

    # create good, set, and save
    good = Good()
    good.owner = request.user
    good.message = good_msg
    good.save()

    # set success message
    messages.success(request, 'You have given good to this message.')
    return redirect(to='/sns/')