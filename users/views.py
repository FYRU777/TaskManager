
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .forms import TaskForm
from .models import Task
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
# Создаем здесь представления.


def home(request):
    return render(request, "users/home.html")


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def add_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('done')
    else:
        form = TaskForm()

    return render(request, 'users/add_task.html', context={'form': form})


def done(request):
    return render(request, 'users/done.html')


def show_all_tasks(request):
    tasks = Task.objects.filter(user_id=request.user.id)
    data = {
        'tasks': tasks
    }
    return render(request, 'users/all_tasks.html', context=data)


def show_one_task(request, task_id):
    task = Task.objects.get(id=task_id)

    data = {
        'task': task,
    }
    return render(request, 'users/task.html', context=data)
