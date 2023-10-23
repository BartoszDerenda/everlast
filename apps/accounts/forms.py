from django import forms


class CreateComment(forms.Form):
    rep = (
        (1, 'Positive'),
        (0, 'Neutral'),
        (-1, 'Negative')
    )
    text = forms.CharField(widget=forms.Textarea(attrs={"rows": "5"}), max_length=255, label='')
    points = forms.CharField(widget=forms.Select(choices=rep), label='')
