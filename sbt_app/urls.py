from django.urls import path
from sbt_app import views

urlpatterns = [
    path("", views.home, name="home"),
]