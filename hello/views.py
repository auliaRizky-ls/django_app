from django.shortcuts import render
#from django.views.generic import TemplateView
from .models import Friend
from django.db.models import QuerySet

def __new_str__(self):
    result = ''
    for item in self:
        result += '<tr>'
        for k in item:
            result += '<td>' + str(k) + '=' + str(item[k]) + '</td>'
        result += '<tr>'
    return result

QuerySet.__str__ = __new_str__

def index(request):
    data = Friend.objects.all().values("id", "name", "age")
    params = {
        "title" : "Hello",
        "data" : data,
    }
    return render(request, "hello/index.html", params)

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