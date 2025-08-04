from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return Task.objects.all().order_by('-created_at')

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'status', 'due_date']
    success_url = reverse_lazy('tasks:task_list')

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'status', 'due_date']
    
    def get_success_url(self):
        return reverse_lazy('tasks:task_detail', kwargs={'pk': self.object.pk})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('tasks:task_list')