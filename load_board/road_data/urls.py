from django.urls import path

from . import views

urlpatterns = [
    path("readMsg/", views.read_message, name="read_message"),
]