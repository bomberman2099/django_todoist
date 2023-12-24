from django.db import models


class TodoList(models.Model):
    TodoItem = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.TodoItem[:30]

