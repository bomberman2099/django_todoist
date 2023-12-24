from django.shortcuts import render
from django.views import View

from todolist_app.models import TodoList


class TodoListView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        form = request.POST.get('form')
        if form:
            todolist = TodoList.objects.create(TodoItem=form)
            todolist.save()
        return render(request, 'index.html')