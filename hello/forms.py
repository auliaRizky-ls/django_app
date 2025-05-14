from django import forms

HOBBY_CHOICES = [
    ('reading', '読書'),
    ('sports', 'スポーツ'),
    ('music', '音楽'),
]

COLOR_CHOICES = [
    ('red', '赤'),
    ('blue', '青'),
    ('green', '緑'),
]

class HelloForm(forms.Form):
    hobbies = forms.MultipleChoiceField(
        label="趣味を選んでください（複数可）：",
        choices=HOBBY_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'})
    )

    color = forms.ChoiceField(
        label="好きな色を選んでください：",
        choices=COLOR_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
    )

    birthdate = forms.DateField(
        label="誕生日：",
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )