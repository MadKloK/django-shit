from django.urls import path
from app2.views import *

app_name = "app2"

urlpatterns = [
    path('blog/',  blog_view, name="index"),
    path('blog/single/', blog_single, name="single"),
]
