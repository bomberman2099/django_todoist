from django.contrib.auth.models import User
from django.db import models


class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    TodoItem = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.TodoItem[:30]

