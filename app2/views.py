from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from app2.models import Post

# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(published_at__lte=timezone.now(), status=True)
    context = {'posts': posts}
    return render(request, "app2/blog-home.html", context)

def blog_single(request, pid):
    post = get_object_or_404(Post, id=pid)
    context = {'post': post}

    post.views_count += 1
    post.save()

    return render(request, "app2/blog-single.html", context)

# def test(request, pid):
#     post = get_object_or_404(Post, id=pid)
#     context = {'post': post}

#     post.views_count += 1
#     post.save()

#     return render(request, 'app2/test.html', context)