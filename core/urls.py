from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('register',register,name='register'),
    path('login',log_in,name='login'),
    path('logout',log_out,name='logout'),
    path('add_todo/',add_todo,name='add_todo'),
    path('delete_todo/<int:pk>/',delete_todo,name='delete_todo'),
    path('edit_todo/<int:pk>/',edit_todo,name='edit_todo'),
]