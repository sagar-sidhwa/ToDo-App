from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='index'),
    path('login/', views.ulogin,name='login'),
    path('logout/', views.ulogout,name='logout'),
    path('register/', views.uregister,name='register'),
    path('userdetails/', views.userdetails,name='userdetails'),
    path('userdetails/<int:id>', views.userdetails,name='userdetails'),
    path('updateuserdetails', views.updateuserdetails,name='updateuserdetails'),
    path('updateuserdetails/<int:id>', views.updateuserdetails,name='updateuserdetails'),
    path('todolist/', views.todolist,name='todolist'),
    path('updatetask/<int:id>', views.updatetask,name='updatetask'),
    path('updatetask', views.updatetask,name='updatetask'),
    path('updatetodolist/<int:id>', views.updatetodolist,name='updatetodolist'),
    path('updatetodolist/', views.updatetodolist,name='updatetodolist'),
    path('deletetodo/<int:id>', views.deletetodo,name='deletetodo'),
]