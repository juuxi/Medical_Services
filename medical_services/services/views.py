from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Service


class ServicesListView(ListView):
    model = Service
    ordering = 'id'
    paginate_by = 5


class ServiceDetailView(DetailView):
    model = Service
    pk_url_kwarg = 'service_id'
    template_name = 'services/service_detail.html'

