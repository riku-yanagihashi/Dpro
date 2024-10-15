from django.urls import path

from . import views

app_name = "VTDbank"

urlpatterns = [
    path("", views.Index, name="index"),
    path("admin/", views.Admin, name="admin"),
    path("register/", views.Register, name="register"),
    path("graph/", views.Graph, name="graph"),
    path("claim/", views.Claim, name="claim"),
    path("payclaim/<int:id>/", views.PayClaim, name="payclaim"),
    path("logs/", views.Logs, name="logs"),
    path("graph/all/", views.AllGraph, name="allgraph"),
]