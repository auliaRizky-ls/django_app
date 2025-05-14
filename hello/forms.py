from django import forms

class HelloForm(forms.Form):
    # name = forms.CharField(label = "name", required = True, widget = forms.TextInput(attrs={"class":"form-control"}))
    # mail = forms.EmailField(label = "mail", widget = forms.EmailInput(attrs={"class":"form-control"}))
    # age = forms.IntegerField(label = "age", min_value = 0, max_value = 100, widget = forms.NumberInput(attrs={"class":"form-control"}))
    # val = forms.FloatField(label = "val", min_value = 0, max_value = 100, widget = forms.NumberInput(attrs={"class":"form-control"}))
    # url = forms.URLField(label = "url", widget = forms.URLInput(attrs={"class":"form-control"}))
    # d1 = forms.DateField(label = "date", required = True, widget = forms.DateInput(attrs={"class":"form-control"}))
    # t1 = forms.TimeField(label = "time", widget = forms.TimeInput(attrs={"class":"form-control"}))
    # dt1 = forms.DateTimeField(label = "datetime", widget = forms.DateTimeInput(attrs={"class":"form-control"}))
    # check = forms.BooleanField(label = "Checkbox", required = False)
    # check = forms.NullBooleanField(label = "Check")

    data = [
        ("one", "item 1"),
        ("two", "item 2"),
        ("three", "item 3"),
        ("four", "item 4"),
        ("five", "item 5")
    ]
    choice = forms.MultipleChoiceField(label = "radio", choices = data, widget = forms.SelectMultiple(attrs={"size": 6, "class":"form-select"}))