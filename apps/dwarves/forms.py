from django import forms

from apps.accounts.models import Account, Treasury
from apps.items.models import Item, Armor


class CreateWarband(forms.Form):
    dwarf1_quirk1 = (
        ('Strong', "strongest"),
        ('Wise', " wisest"),
        ('Agile', "most nimble"),
        ('Hefty', "heftiest")
    )

    dwarf1_quirk2 = (
        ('Strong', "out-drinks us all"),
        ('Wise', "gives us tips"),
        ('Agile', "steals one of my beers"),
        ('Charismatic', "sings and flirts")
    )

    dwarf2_quirk1 = (
        ('Strong', "He was one of immense girth."),
        ('Wise', "Although he couldn't keep up on a mountain trekk, he excelled in arcane studies."),
        ('Agile', "He used to pull mean pranks on his Primus but never got caught."),
        ('Lucky', "Lucky placeholder.")
    )

    dwarf2_quirk2 = (
        ('Strong', "He was one of immense girth."),
        ('Wise', "Although he couldn't keep up on a mountain trekk, he excelled in arcane studies."),
        ('Agile', "He used to pull mean pranks on his Primus but never got caught."),
        ('Lucky', "Lucky placeholder.")
    )

    dwarf3_quirk1 = (
        ('Strong', "He was one of immense girth."),
        ('Wise', "Although he couldn't keep up on a mountain trekk, he excelled in arcane studies."),
        ('Agile', "He used to pull mean pranks on his Primus but never got caught."),
        ('Lucky', "Lucky placeholder.")
    )

    dwarf3_quirk2 = (
        ('Strong', "He was one of immense girth."),
        ('Wise', "Although he couldn't keep up on a mountain trekk, he excelled in arcane studies."),
        ('Agile', "He used to pull mean pranks on his Primus but never got caught."),
        ('Lucky', "Lucky placeholder.")
    )

    dwarf4_quirk1 = (
        ('Strong', "of Irongrip"),
        ('Wise', " the Wise"),
        ('Agile', " the Nimble"),
        ('Lucky', "that lucky bastard")
    )

    dwarf4_quirk2 = (
        ('Strong', "fell into druid's cauldron when they were brewing a magic potion"),
        ('Wise', "managed to decipher those elven runes when you got trapped in the ruins"),
        ('Agile', "somehow disarmed that entire gauntlet full of traps all by himself"),
        ('Lucky', "kept the witch busy with his gossip as we planned our ambush")
    )

    dwarf5_quirk1 = (
        ('Strong', "He was one of immense girth."),
        ('Wise', "Although he couldn't keep up on a mountain trekk, he excelled in arcane studies."),
        ('Agile', "He used to pull mean pranks on his Primus but never got caught."),
        ('Lucky', "Lucky placeholder.")
    )

    dwarf5_quirk2 = (
        ('Strong', "He was one of immense girth."),
        ('Wise', "Although he couldn't keep up on a mountain trekk, he excelled in arcane studies."),
        ('Agile', "He used to pull mean pranks on his Primus but never got caught."),
        ('Lucky', "Lucky placeholder.")
    )

    dwarf1_name = forms.CharField(label='', max_length=32)
    dwarf1_quirk1 = forms.CharField(widget=forms.Select(choices=dwarf1_quirk1), label='')
    dwarf1_quirk2 = forms.CharField(widget=forms.Select(choices=dwarf1_quirk2), label='')

    dwarf2_name = forms.CharField(label='', max_length=32)
    dwarf2_quirk1 = forms.CharField(widget=forms.Select(choices=dwarf2_quirk1), label='')
    dwarf2_quirk2 = forms.CharField(widget=forms.Select(choices=dwarf2_quirk2), label='')

    dwarf3_name = forms.CharField(label='', max_length=32)
    dwarf3_quirk1 = forms.CharField(widget=forms.Select(choices=dwarf3_quirk1), label='')
    dwarf3_quirk2 = forms.CharField(widget=forms.Select(choices=dwarf3_quirk2), label='')

    dwarf4_name = forms.CharField(label='', max_length=32)
    dwarf4_quirk1 = forms.CharField(widget=forms.Select(choices=dwarf4_quirk1), label='')
    dwarf4_quirk2 = forms.CharField(widget=forms.Select(choices=dwarf4_quirk2), label='')

    dwarf5_name = forms.CharField(label='', max_length=32)
    dwarf5_quirk1 = forms.CharField(widget=forms.Select(choices=dwarf5_quirk1), label='')
    dwarf5_quirk2 = forms.CharField(widget=forms.Select(choices=dwarf5_quirk2), label='')


class EquipmentForm(forms.ModelForm):

    def __init__(self, user_id, *args, **kwargs):
        super(EquipmentForm, self).__init__(*args, **kwargs)
        self.user_id = user_id
        # self.fields['items'].queryset = Treasury.objects.filter(user=self.request.user)

    class Meta:
        model = Treasury
        fields = ['name', 'quantity']

    name = forms.CharField()
    quantity = forms.IntegerField()

