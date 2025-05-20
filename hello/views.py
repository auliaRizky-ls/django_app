from django.shortcuts import render
from django.shortcuts import redirect
#from django.views.generic import TemplateView
from .forms import FriendForm
from .forms import FindForm
from .models import Friend
from django.views.generic import ListView
from django.views.generic import DetailView
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Min, Max

class FriendList(ListView):
    model = Friend

class FriendDetail(DetailView):
    model = Friend

def index(request):
    data = Friend.objects.all()
    re1 = Friend.objects.aggregate(Count("age"))
    re2 = Friend.objects.aggregate(Sum("age"))
    re3 = Friend.objects.aggregate(Avg("age"))
    re4 = Friend.objects.aggregate(Min("age"))
    re5 = Friend.objects.aggregate(Max("age"))
    msg = 'count: ' + str(re1['age__count']) + ',<br>sum: ' + str(re2['age__sum']) + ', <br>avg: ' + str(re3['age__avg']) + ', <br>min: ' + str(re4['age__min']) + ', <br>max: ' + str(re5['age__max'])
    params = {
        "title" : "Hello",
        "message" : msg,
        "data" : data,
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