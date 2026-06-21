from django.shortcuts import render

# Create your views here.

def blog_view(request):
    return render(request, "app2/blog-home.html")

def blog_single(request):
    return render(request, "app2/blog-single.html")