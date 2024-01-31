from . import views
from django.urls import path

urlpatterns = [
    path('addTask/', views.addTask,name='addTask'),
    path('markasdone/<int:pk>/', views.mark_as_done , name="markasdone"),
    path('edittask/<int:pk>/', views.edit_task, name="edittask"),
    path('deletetask/<int:pk>/', views.delete_task, name="deletetask"),
    path('markasundone/<int:pk>/', views.mark_as_undone , name="markasundone"),
]