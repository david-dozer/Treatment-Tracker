from django.urls import path
from abat import views

urlpatterns = [
    # path("", views.home, name="home"),
    path('', views.start_screen, name='start-screen'),
    path('start_treatment/', views.start_treatment, name='start_treatment'),
    path('<str:name>/', views.hello_there, name='hello_there') 
]