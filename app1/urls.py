from django.urls import path
from app1.views import *

app_name = "app1"

urlpatterns = [
    path('about/',  about_view, name="about"),
    path('contact/', contact_view, name="contact"),
    path('elements/', elements_view, name="elements"),
    path('', home_view, name="index"),
    path('test/', test, name='test')
]
