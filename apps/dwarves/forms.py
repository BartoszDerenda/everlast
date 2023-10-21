from django import forms


class CreateWarbandForm(forms.Form):
    name = forms.CharField(label='Name', max_length=32)