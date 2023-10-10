from django.urls import path

from todoapp import views

urlpatterns=[
    path('',views.mainpage,name='mainpage'),
    path('addTodo', views.addTodo, name="addTodo"),
    path('viewtodo', views.viewtodo, name="viewtodo"),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),

]