from django.urls import path
from . import views

urlspatterns = [
    path(' ', views.task_list, name = 'task_list')
]