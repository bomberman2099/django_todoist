from django.shortcuts import render, redirect, reverse
from django.views import View

from todolist_app.models import TodoList


class TodoListView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('user:login')
        todolist = TodoList.objects.filter(user=request.user)

        return render(request, 'index.html', context={'todolist': todolist})

    def post(self, request):
        form = request.POST.get('form')
        if form:
            todolist = TodoList.objects.create(TodoItem=form, status=False, user=request.user)
            todolist.save()
        todolist = TodoList.objects.filter(user=request.user)
        return render(request, 'index.html', {'todolist': todolist})

def DeleteTodo(request, pk):
    t = TodoList.objects.get(id=pk)
    t.delete()
    return redirect(reverse('home_app:home'))


def FinishTodo(request, pk):
    t = TodoList.objects.get(id=pk)
    t.status = True
    t.save()
    return redirect(reverse('home_app:home'))

