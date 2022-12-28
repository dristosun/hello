from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addFlight", views.addFlight, name="addFlight"),
    path("flight/<int:flightId>", views.flight, name="flight")
]