from django import template
from app2.models import Post

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