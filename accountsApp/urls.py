from django.urls import path
from .views import *

urlpatterns = [
    path("nav" , nav , name = "nav"),
]
