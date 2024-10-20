from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [ #prima coloana e db value a doua e human value
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField()
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='low')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
