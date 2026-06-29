from django import template
from app2.models import Post, Category

register = template.Library()

@register.simple_tag(name='get_posts')
def get_posts():
    posts = Post.objects.filter(status=True)
    return posts

@register.filter(name='snippet')
def snippet(content, arg):
    return content[:arg+1] + ' ...'

@register.inclusion_tag('app2/blog-latest-posts.html', name='latest_posts')
def latest_posts(total=4):
    posts = Post.objects.filter(status=True).order_by('published_at')[:total + 1]
    return {'posts': posts}

@register.inclusion_tag('app2/blog-post-category.html', name='categories_count')
def categories_count(total=7):
    posts = Post.objects.filter(status=1).prefetch_related('category')
    cat_dict = {}

    for post in posts:
        for cat in post.category.all():
            cat_dict[cat.name] = cat_dict.get(cat.name, 0) + 1

    return {'categories_count': list(cat_dict.items())[:total]}