from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from todo.models import Task
from todo.forms import TaskForm


class TaskListView(generic.ListView):
    model = Task
    template_name = "todo/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todoapp/task_form.html"
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")





