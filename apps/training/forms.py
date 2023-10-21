from django import forms


class TrainingForm(forms.Form):
    attribute = forms.CharField(label='attribute', max_length=100)
    method = forms.CharField(label='method', max_length=100, widget=forms.Textarea)
