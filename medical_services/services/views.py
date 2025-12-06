from django.shortcuts import render

def service_list(request):
    return render(request, 'services/services_list.html')


def service(request, service_id):
    return render(request, 'core/homepage.html')
