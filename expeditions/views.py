from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/mountain', redirect_field_name=None)
def expeditions(request):
    return render(request, "expeditions/expeditions.html", {})
