from django.urls import path
from abat import views

urlpatterns = [
    path("", views.home, name="home"),
    path("abat/<name>", views.hello_there, name="hello_there")
]