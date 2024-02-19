from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("siddhant", views.siddhant, name="siddhant"),
    path("<str:name>", views.greet, name="greet")
]