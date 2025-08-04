from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from django.utils import timezone

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('tasks:task_detail', args=[str(self.id)])
    
    def is_overdue(self):
        if self.due_date:
            return timezone.now().date() > self.due_date
        return False
    
    class Meta:
        ordering = ['-created_at']