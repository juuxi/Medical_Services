from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import News


class NewsListView(ListView):
    model = News
    ordering = 'created_at'


class NewsDetailView(DetailView):
    model = News
    pk_url_kwarg = 'news_id'
    template = 'news/news_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_news'] = News.objects.filter(Q(is_published=True) &
                                                     ~Q(pk=self.object.pk)).order_by('-created_at')[:4]
        return context