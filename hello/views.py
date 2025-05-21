from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
#from django.views.generic import TemplateView
from .forms import FriendForm, MessageForm
from .forms import FindForm
from .forms import CheckForm
from .models import Friend, Message
from django.views.generic import ListView
from django.views.generic import DetailView

class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend

def index(request, num = 1):
    data = Friend.objects.all()
    page = Paginator(data, 3)
    params = {
        "title" : "Hello",
        "message" : "",
        "data" : page.get_page(num),
    }
    return render(request, "hello/index.html", params)

def create(request):
    if (request.method == "POST"):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to="/hello")
    params = {
        "title" : "Hello",
        "form" : FriendForm()
    }
    return render(request, 'hello/create.html', params)

def edit(request, num):
    obj = Friend.objects.get(id = num)
    if (request.method == "POST"):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        "title" : "Hello",
        'id' : num,
        "form" : FriendForm(instance=obj),
    }
    return render(request, 'hello/edit.html', params)

def delete(request, num):
    friend = Friend.objects.get(id=num)
    if (request.method == "POST"):
        friend.delete()
        return redirect(to='/hello')
    params = {
        "title" : "Hello",
        "id" : num,
        "obj" : friend,
    }
    return render(request, 'hello/delete.html', params)

def find(request):
    if (request.method == "POST"):
        msg = request.POST["find"]
        form = FindForm(request.POST)
        sql = 'select * from hello_friend'
        if msg != "":
            sql += ' where ' + msg
        data = Friend.objects.raw(sql)
        msg = sql
    else:
        msg = "search words..."
        form = FindForm()
        data = Friend.objects.all()
    params = {
        "title" : "Hello",
        "message" : msg,
        "form" : form,
        "data" : data,
    }
    return render(request, 'hello/find.html', params)

def check(request):
    params = {
        "title" : "Hello",
        "message" : "check validation.",
        "form" : FriendForm(),
    }
    if (request.method == "POST"):
        obj = Friend()
        form = FriendForm(request.POST, instance=obj)
        params["form"] = form
        if form.is_valid():
            params["message"] = "valid."
        else:
            params["message"] = "invalid."
    return render(request, 'hello/check.html', params)

def message(request, num=1):  
    if (request.method == "POST"):
        obj = Message()
        form = MessageForm(request.POST, instance=obj)
        form.save()
        return redirect('message', num=num) 
    data = Message.objects.all().reverse()
    paginator = Paginator(data, 5)
    params = {
        "title" : "Message",
        "form" : MessageForm(),
        "data" : paginator.get_page(num),  
    }
    return render(request, 'hello/message.html', params)

# class HelloView(TemplateView):
#     def __init__(self):
#         self.params = {
#             "title" : "Hello",
#             "form" : SessionForm(),
#             "result" : None
#         }

#     def get(self, request):
#         self.params["result"] = request.session.get("last_msg", "No message.")
#         return render(request, "hello/index.html", self.params)
    
#     def post(self, request):
#         ses = request.POST["session"]
#         self.params["result"] = 'send: "' + ses + '".'
#         request.session["last_msg"] = ses
#         self.params["form"] = SessionForm(request.POST)
#         return render(request, "hello/index.html", self.params)

# def sample_middleware(get_response):
#     def middleware(request):
#         counter = request.session.get("counter", 0)
#         request.session["counter"] = counter + 1
#         response = get_response(request)
#         print("count: " + str(counter))
#         return response
#     return middleware