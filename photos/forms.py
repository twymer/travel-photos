from django import forms

class PhotoForm(forms.Form):
    title = forms.CharField(max_length=50)
    image = forms.ImageField(
        label='Select a file'
    )
