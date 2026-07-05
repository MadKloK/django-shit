from django.urls import path
from django.contrib.sitemaps.views import sitemap

from app1.sitemaps import StaticViewSitemap
from app2.sitemaps import App2Sitemap
from app1.views import *

app_name = "app1"

sitemaps = {
    "static": StaticViewSitemap,
    'app2': App2Sitemap
}

urlpatterns = [
    path('about/',  about_view, name="about"),
    path('contact/', contact_view, name="contact"),
    path('elements/', elements_view, name="elements"),
    path('newsletter/', newsletter_view, name="newsletter"),
    path('', home_view, name="index"),
    path('test/', test, name='test'),
    path(
        "sitemap.xml", sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    )
]
