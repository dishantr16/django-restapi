from django.urls import path
from .views import json_example_view,JsonCBV,JsonCBV2
from django.conf.urls import url

urlpatterns = [
    path('',json_example_view),
    path('cbv/',JsonCBV.as_view()),
    path('cbv2/',JsonCBV2.as_view()),
]