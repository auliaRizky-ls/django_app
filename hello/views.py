from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm

class HelloView(TemplateView):
    def __init__(self):
        self.params = {
            "title" : "Hello",
            "message" : "Please Insert Your Data:",
            "form" : HelloForm(),
            "result" : None
        }

    def get(self, request):
        return render(request, "hello/index.html", self.params)
    
    def post(self, request):
        msg = 'Your name is, <b>' + request.POST["name"] + \
        '(' + request.POST["age"] + ').'
        ch = request.POST["choice"]
        mail = request.POST["mail"]
        password = "(表示しません)"
        self.params["result"] = msg + ' Your gender is, ' + ch + '.<br>' 'Your email address is, ' + mail + '.<br>' 'And, your password is, ' + password + '.'
        self.params["form"] = HelloForm()
        return render(request, "hello/index.html", self.params)