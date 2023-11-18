from django.urls import path

from . import views

urlpatterns = [
    path("readMsg/", views.read_message, name="read_message"),
    path("seeTrucks/", views.see_dataTruck, name="seeTrucks"),
    path("seeLoads/", views.see_dataLoad, name="seeLoads")
]