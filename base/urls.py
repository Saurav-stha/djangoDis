from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('server/<str:sid>/',views.server , name="server"),

    path('create-server' , views.createServer, name="create-server"),
    path('update-server/<str:pk>/' , views.updateServer, name="update-server"),
    path('delete-server/<str:pk>/' , views.deleteServer, name="delete-server"),
]