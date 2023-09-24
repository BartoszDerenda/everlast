from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/mountain', redirect_field_name=None)
def marketplace(request):
    return render(request, "marketplace/marketplace.html", {})