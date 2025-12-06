from django.shortcuts import render

from django.views.generic import TemplateView

class HomepageView(TemplateView):
    template_name = 'core/homepage.html'

class AboutView(TemplateView):
    template_name = 'core/about.html'
