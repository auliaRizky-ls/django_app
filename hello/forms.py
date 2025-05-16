from django import forms
from .models import Friend

class HelloForm(forms.Form):
    id = forms.IntegerField(label = "ID", min_value = 1, max_value = Friend.objects.all().count())

class SessionForm(forms.Form):
    session = forms.CharField(label = "session", required = False, widget = forms.TextInput(attrs={"class":"form-control"}))