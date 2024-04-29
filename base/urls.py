from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('server/<str:sid>/',views.server , name="server"),

    path('create-server' , views.createServer, name="create-server")
]