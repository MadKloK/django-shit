from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import timezone
from app2.models import Post


class App2Sitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=True, published_at__lte=timezone.now())

    def lastmod(self, obj):
        return obj.published_at
    
    def location(self, item):
        return reverse('app2:single', kwargs={'pid': item.id})