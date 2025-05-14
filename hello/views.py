from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import HelloForm

class HelloView(TemplateView):
    def __init__(self):
        self.params = {
            "title" : "Hello",
            "message" : "What are your hobbies:",
            "form" : HelloForm(),
            "result" : None
        }

    def get(self, request):
        return render(request, "hello/index.html", self.params)
    
    def post(self, request):
        form = HelloForm(request.POST)
        if form.is_valid():
            hobbies = form.cleaned_data['hobbies']
            color = form.cleaned_data['color']
            birthdate = form.cleaned_data['birthdate']
            
            # Convert values to display labels
            hobby_dict = dict(form.fields['hobbies'].choices)
            color_dict = dict(form.fields['color'].choices)
            self.params["result"] = {
                'hobbies': [hobby_dict[h] for h in hobbies],
                'color': color_dict[color],
                'birthdate': birthdate,
            }
        else:
            self.params["result"] = None
        self.params["form"] = HelloForm()
        return render(request, "hello/index.html", self.params)
