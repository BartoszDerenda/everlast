from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.dwarves.models import Dwarf


@login_required(login_url='/mountain', redirect_field_name=None)
def expeditions(request):
    warband = Dwarf.objects.values('id', 'name', 'status').filter(leader=request.user)
    return render(request, "expeditions/expeditions.html", {"warband": warband})
