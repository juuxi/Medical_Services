from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q

from services.models import Service
from news.models import News

class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.filter(Q(is_provided=True))[:4]
        context['news_list'] = News.objects.filter(Q(is_published=True))[:4]
        return context
    

class AboutView(TemplateView):
    template_name = 'core/about.html'
