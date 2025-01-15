from django.shortcuts import render
from .models import Task

def task_list(request):
    tasks = tasks.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})
