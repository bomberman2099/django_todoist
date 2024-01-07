from django.shortcuts import render, redirect, reverse
from django.views import View
<<<<<<< HEAD

=======
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from todolist_app.forms import TodoForm
>>>>>>> e6bd649 (add update task)
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

<<<<<<< HEAD
=======
# class UpdateTodo(UpdateView):
#     model = TodoList
#     fields = ('TodoItem',)
#     template_name = 'update_TodoItem.html'
#     success_url = reverse_lazy('home_app:home')

def UpdateTodoView(request, pk):
    t = TodoList.objects.get(id=pk)
    form = TodoForm(instance=t)
    print(1)
    if request.method == 'POST':
        print(1)
        form = TodoForm(data=request.POST)
        if form.is_valid():
            print(1)
            form.save()
            t.TodoItem = form.cleaned_data.get('TodoItem')
            print(form.cleaned_data.get('TodoItem'))
            t.save()
            return redirect(reverse('home_app:home'))
    return render(request, 'update_TodoItem.html', context={'form': form})
>>>>>>> e6bd649 (add update task)
