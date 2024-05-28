from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('register/',views.registerPage, name="register"),

    path('',views.home, name="home"),
    path('server/<str:sid>/',views.server , name="server"),

    path('profile/<str:pk>/', views.userProfile, name='user-profile'),

    path('create-server' , views.createServer, name="create-server"),
    path('join-server/<str:pk>/' , views.joinServer, name="join-server"),
    path('leave-server/<str:pk>/' , views.leaveServer, name="leave-server"),
    path('update-server/<str:pk>/' , views.updateServer, name="update-server"),
    path('delete-server/<str:pk>/' , views.deleteServer, name="delete-server"),

    path('delete-msg/<str:pk>/' , views.deleteMsg, name="delete-msg"),

    path('update-user/', views.updateUser, name="update-user"),

    path('topics/', views.topicsPage, name="topics"),
    path('activity', views.activityPage, name="activity"),

]