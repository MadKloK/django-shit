from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app2.models import Post

def home_view(request):
    return render(request, 'app1/index.html')

def about_view(request):
    return render(request, 'app1/about.html')

def contact_view(request):
    return render(request, "app1/contact.html")

def elements_view(request):
    return render(request, "app1/elements.html")

def test(request):
#     posts = Post.objects.all()
#     context = {'posts': posts}
    return render(request, 'app1/test.html')