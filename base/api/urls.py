from django.urls import path
from . import views 

urlpatterns = [
    path('', views.getRoutes),
    path('servers/', views.getServers),
    path('servers/<str:pk>/', views.getSingleServer)
]