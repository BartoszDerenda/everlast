from django import forms


class CreateComment(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows": "5"}), max_length=255, label='')
