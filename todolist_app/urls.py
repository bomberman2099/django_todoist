from django.urls import path
from . import views
urlpatterns = [
    path('', views.TodoListView.as_view(), name='home'),
    path('delete/<int:pk>', views.DeleteTodo, name='delete'),
    path('finish/<int:pk>', views.FinishTodo, name='finishing'),
]