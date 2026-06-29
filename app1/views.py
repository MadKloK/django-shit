from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.paginator import Paginator
from django.utils import timezone
from app2.models import Post

def home_view(request):
    posts = Post.objects.filter(
        status=True,
        published_at__lte=timezone.now()
        ).order_by('-published_at')[:6].prefetch_related('category') # prefetch because of the query for categories in the template

    context = {'posts': posts}
    return render(request, 'app1/index.html', context)

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