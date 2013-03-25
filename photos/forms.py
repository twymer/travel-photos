from django import forms

class PhotoForm(forms.Form):
    image = forms.FileField(
        label='Select a file'
    )
