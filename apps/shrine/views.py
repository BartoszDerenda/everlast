from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.dwarves.models import Dwarf


@login_required(login_url='/mountain', redirect_field_name=None)
def shrine(request):
    warband = Dwarf.objects.filter(leader=request.user).values('id', 'name', 'status')
    return render(request, 'shrine/shrine.html', {'warband': warband})
