from django.urls import path
from . import views
<<<<<<< HEAD
app_name = 'home_app'
=======

app_name = 'home_app'

>>>>>>> e6bd649 (add update task)
urlpatterns = [
    path('', views.TodoListView.as_view(), name='home'),
    path('delete/<int:pk>', views.DeleteTodo, name='delete'),
    path('finish/<int:pk>', views.FinishTodo, name='finishing'),
<<<<<<< HEAD
=======
    path('update/<int:pk>', views.UpdateTodoView, name='update'),
>>>>>>> e6bd649 (add update task)
]