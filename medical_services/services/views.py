from django.shortcuts import render

def service_list(request):
    return render(request, 'core/homepage.html')


def service(request, service_id):
    return render(request, 'core/homepage.html')
