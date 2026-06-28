from django.urls import path
from app2.views import *

app_name = "app2"

urlpatterns = [
    path('',  blog_view, name="index"),
    path('<int:pid>/', blog_single, name="single"),
    path('test/', test, name='test')
]
