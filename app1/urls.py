from django.urls import path
from app1.views import *

app_name = "app1"

urlpatterns = [
    path('http-test/', http_test),
    path('json-test/', json_test),
    path('about/',  about_view, name="about"),
    path('contact/', contact_view, name="contact"),
    path('elements/', elements_view, name="elements"),
    path('', home_view, name="index"),
]
