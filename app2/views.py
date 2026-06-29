from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.utils import timezone
from app2.models import Post

# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(published_at__lte=timezone.now(), status=True)
    context = {'posts': posts}
    return render(request, "app2/blog-home.html", context)

def blog_single(request, pid):
    posts = Post.objects.filter(published_at__lte=timezone.now(), status=True)
    post = get_object_or_404(posts, id=pid)

    post.views_count = F('views_count') + 1
    post.save(update_fields=['views_count'])
    post.refresh_from_db() # this gives a real value not F object, PLUS if you dont update and save another time, it would do the increment twice!!!

    previous_post = posts.filter(published_at__lt=post.published_at).order_by('-published_at').first()
    next_post = posts.filter(published_at__gt=post.published_at).order_by('published_at').first()

    context = {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post
        }

    return render(request, "app2/blog-single.html", context)

def blog_category(request, cat_name):
    posts = Post.objects.filter(status=True, category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'app2/blog-home.html', context)

# def test(request, pid):
#     post = get_object_or_404(Post, id=pid)
#     context = {'post': post}

#     post.views_count += 1
#     post.save()

#     return render(request, 'app1/test.html', context)