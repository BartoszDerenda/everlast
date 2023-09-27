from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.dwarves.models import Dwarf


@login_required(login_url='/mountain', redirect_field_name=None)
def training(request):
    warband = Dwarf.objects.values('name', 'status').filter(leader=request.user)
    training_types = {
        "strength": {
            "method": {
                "name": "Throwing rocks",
                "cost": {
                    "Ziele trytonów": 5,
                    "Jaskółcze ziele": 5,
                    "Oakbrew": 5,
                },
                "time_and_result": {
                    "Time": "15 min",
                    "Result": 1
                },
            }
        },
        "intelligence": {
            "method": {
                "name": "Crosswords",
                "cost": {
                    "Niezapominajki": 5,
                    "Jaskółcze ziele": 5,
                    "Oakbrew": 5,
                },
                "time_and_result": {
                    "Time": "15 min",
                    "Result": 1
                },
            },
        }
    }

    return render(request, "training/training.html", {"warband": warband,
                                                      "training_types": training_types})
