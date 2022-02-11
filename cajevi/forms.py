from django import forms

# Create your forms here.

class CheckBox(forms.Form):
    Nana = forms.BooleanField()
    Kamilica = forms.BooleanField()
    Herbal = forms.BooleanField()