from django import forms

class REviewForm(forms.Form):
    name = forms.CharField(
        label = 'Firstname', min_length=4, max_length=50, widgth
    )