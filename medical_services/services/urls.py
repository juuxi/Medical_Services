from django.urls import path

from . import views

app_name = 'services'

urlpatterns = [
    path('<int:service_id>/', views.service, name="service"),
    path('', views.service_list, name="services_list"),
]
