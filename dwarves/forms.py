from django import forms


class CreateWarbandForm(forms.Form):
    dwarf_name1 = forms.CharField(label='Name', max_length=64)
    dwarf_name2 = forms.CharField(label='Name', max_length=64)
    dwarf_name3 = forms.CharField(label='Name', max_length=64)