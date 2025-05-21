from django import forms
from .models import Friend, Message

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']
        widgets = {
            'name': forms.TextInput(attrs={"class":"form-control"}),
            'mail': forms.EmailInput(attrs={"class":"form-control"}),
            'age': forms.NumberInput(attrs={"class":"form-control"}),
            'birthday': forms.DateInput(attrs={"class":"form-control"}),
        }

class FindForm(forms.Form):
    find = forms.CharField(label = "find", required = False, widget = forms.TextInput(attrs={"class":"form-control"}))

class HelloForm(forms.Form):
    name = forms.CharField(label = "Name", widget = forms.TextInput(attrs={"class":"form-control"}))
    mail = forms.EmailField(label = "Email", widget = forms.EmailInput(attrs={"class":"form-control"}))
    gender = forms.BooleanField(label = "Gender", required = False, widget = forms.CheckboxInput(attrs={"class":"form-check"}))
    age = forms.IntegerField(label = "Age", widget = forms.NumberInput(attrs={"class":"form-control"}))
    birthday = forms.DateField(label = "Birthday", widget = forms.DateInput(attrs={"class":"form-control"}))

class SessionForm(forms.Form):
    session = forms.CharField(label = "session", required = False, widget = forms.TextInput(attrs={"class":"form-control"}))

class CheckForm(forms.Form):
    str = forms.CharField(label = "String", widget = forms.TextInput(attrs={"class":"form-control"}))

    def clean(self):
        cleaned_data = super().clean()
        str = cleaned_data.get("str")
        if (str.lower().startswith("no")):
            raise forms.ValidationError("You input no.")
        return cleaned_data

# create a class based on the Message model
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['friend', 'title', 'content']
        widgets = {
            'friend': forms.Select(attrs={"class":"form-control"}),
            'title': forms.TextInput(attrs={"class":"form-control"}),
            'content': forms.Textarea(attrs={"class":"form-control"}),
        }