from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(label = "name", required = True, widget = forms.TextInput(attrs={"class":"form-control"}))
    age = forms.IntegerField(label = "age", widget = forms.NumberInput(attrs={"class":"form-control"}))
    
    data = [
        ("apache helicopter", "Apache Helicopter"),
        ("male", "Male"),
        ("female", "Female")
    ]
    choice = forms.ChoiceField(label = "choice", choices = data)
    mail = forms.EmailField(label = "mail", required = True, widget = forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label = "password", required = True, widget = forms.TextInput(attrs={"class":"form-control"}))