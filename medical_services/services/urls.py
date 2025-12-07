from django.urls import path

from . import views

app_name = 'services'

urlpatterns = [
    path('service/<int:service_id>/', views.ServiceDetailView.as_view(), name="service_detail"),
    path('', views.ServicesListView.as_view(), name="services_list"),
]
