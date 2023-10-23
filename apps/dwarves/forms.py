from django import forms


class CreateWarband(forms.Form):
    quirk = (
        ([5, 5, -3], '+5 Strength, +5 Endurance, -3 Speed'),
        ([-3, 5, 5], '-3 Endurance, +5 Intellect, +5 Willpower'),
        ([5, -3, 5], '+5 Agility, -3 Strength, +5 Speed')
    )
    dwarf1_name = forms.CharField(label='Name', max_length=32)
    dwarf1_quirk = forms.CharField(widget=forms.Select(choices=quirk), label='')

    dwarf2_name = forms.CharField(label='Name', max_length=32)
    dwarf2_quirk = forms.CharField(widget=forms.Select(choices=quirk), label='')

    dwarf3_name = forms.CharField(label='Name', max_length=32)
    dwarf3_quirk = forms.CharField(widget=forms.Select(choices=quirk), label='')

    dwarf4_name = forms.CharField(label='Name', max_length=32)
    dwarf4_quirk = forms.CharField(widget=forms.Select(choices=quirk), label='')

    dwarf5_name = forms.CharField(label='Name', max_length=32)
    dwarf5_quirk = forms.CharField(widget=forms.Select(choices=quirk), label='')
