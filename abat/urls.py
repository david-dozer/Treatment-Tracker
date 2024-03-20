from django.urls import path
from abat import views

urlpatterns = [
    # path("", views.home, name="home"),
    path('', views.start_screen, name='start-screen'),
    path("abat/<name>", views.hello_there, name="hello_there")
]