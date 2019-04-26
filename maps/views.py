import requests
from django.shortcuts import render

from .models import Occurrence


def default_map(request):
    occurrences = Occurrence.objects.all()
    return render(request, 'default.html', {'occurrences': occurrences, 'icon': 'transito_leve'})
