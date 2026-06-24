from django.shortcuts import render
from app2.models import Post

# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(status=True)
    context = {'posts': posts}
    return render(request, "app2/blog-home.html", context)

def blog_single(request):
    return render(request, "app2/blog-single.html")