from django.shortcuts import render
from django.views.generic import ListView

from .models import Service


class ServicesListView(ListView):
    model = Service
    ordering = 'id'


def service(request, service_id):
    return render(request, 'core/homepage.html')
