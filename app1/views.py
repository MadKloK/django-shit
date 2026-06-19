from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def http_test(request):
    return HttpResponse("hey this is the test")

def json_test(request):
    return JsonResponse({'objective': 'test', 'damn': True})

def home_view(request):
    return render(request, 'app1/home.html')

def about_view(request):
    return render(request, 'app1/about.html')