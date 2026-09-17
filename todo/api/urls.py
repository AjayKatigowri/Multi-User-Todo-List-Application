from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.todos_view, name='todos'),
    path('add/', views.add_todo, name='add_todo'),
    path('<int:todo_id>/toggle/', views.toggle_todo, name='toggle_todo'),
    path('<int:todo_id>/delete/', views.delete_todo, name='delete_todo'),
]