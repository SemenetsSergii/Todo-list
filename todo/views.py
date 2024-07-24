from django.shortcuts import render
from django.views import generic

from todo.models import Task
from todo.forms import TaskForm


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm


