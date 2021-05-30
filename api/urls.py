from django.urls import path
from . import views
urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('todo-list/', views.todoList, name="todo-List"),
    path('todo-detail/<str:pk>/', views.todoDetail, name="todo-Detail"),
    path('todo-update/<str:pk>/', views.todoUpdate, name="todo-Update"),
    path('todo-create/', views.todoCreate, name="todo-Create"),
    path('todo-delete/<str:pk>/', views.todoDelete, name="todo-Delete"),
]
