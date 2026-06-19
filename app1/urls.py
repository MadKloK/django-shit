from django.urls import path
from app1.views import *

urlpatterns = [
    path('http-test/', http_test),
    path('json-test/', json_test),
    path('', home_page)
]
