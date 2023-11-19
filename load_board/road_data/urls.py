from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("credits", views.credits, name="credits"),
    path("readMsg/", views.read_message, name="read_message"),
    path("seeTrucks/", views.see_dataTruck, name="seeTrucks"),
    path("seeLoads/", views.see_dataLoad, name="seeLoads"),
    path("seeNotifs/", views.see_dataNotif, name="seeNotifs"),
    path("notifs/",views.updateNotifications,name='notifs'),
    path("start/",views.start_simulation,name='start')

]