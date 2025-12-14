from django.urls import path

from . import views

app_name = 'news'

urlpatterns = [
    path('<int:news_id>', views.NewsDetailView.as_view(), name="news_detail"),
    path('', views.NewsListView.as_view(), name="news_list"),
]