from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import News


class NewsListView(ListView):
    model = News
    ordering = 'id'


class NewsDetailView(DetailView):
    model = News
    pk_url_kwarg = 'news_id'
    template = 'news/news_detail.html'