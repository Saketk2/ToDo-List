from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks, 'form': form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id = task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance = task)
    tasks = Task.objects.all()
    return render(request, 'edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id = task_id)
    task.delete()
    return redirect('task_list')