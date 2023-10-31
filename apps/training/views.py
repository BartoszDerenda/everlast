from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.dwarves.models import Dwarf
from apps.training.forms import TrainingForm


@login_required(login_url='/mountain', redirect_field_name=None)
def training(request):

    if request.method == 'POST':
        form = TrainingForm(request.POST)

        if form.is_valid():
            attribute = form.cleaned_data['attribute']
            method = form.cleaned_data['method']

    warband = Dwarf.objects.filter(leader=request.user).values('id', 'name', 'status')

    form = TrainingForm()

    return render(request, "training/training.html", {
        'warband': warband,
        'form': form,
    })
