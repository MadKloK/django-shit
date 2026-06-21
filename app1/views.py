from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def http_test(request):
    return HttpResponse("hey this is the test")

def json_test(request):
    return JsonResponse({'objective': 'test', 'damn': True})

def home_view(request):
    return render(request, 'app1/index.html')

def about_view(request):
    return render(request, 'app1/about.html')

def contact_view(request):
    return render(request, "app1/contact.html")

def elements_view(request):
    return render(request, "app1/elements.html")