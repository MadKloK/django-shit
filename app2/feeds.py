from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils import timezone
from app2.models import Post


class LatestEntriesFeed(Feed):
    title = "Blog Latest Posts"
    link = "/rss/feed"
    description = "Updates on changes and additions to my lovely blog."

    def items(self):
        return Post.objects.filter(status=True, published_at__lte=timezone.now())[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100] + '...'

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse("app2:single", args=[item.pk])