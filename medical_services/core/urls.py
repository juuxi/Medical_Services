from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name="homepage"),
    path('about/', views.AboutView.as_view(), name="about"),
]
