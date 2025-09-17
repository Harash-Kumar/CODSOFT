# Create your models here.

from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("completed", "Completed"),
        ("deleted", "Deleted"),
    ]

    text = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="active")
    updated_at = models.DateTimeField(auto_now=True)  # auto-updates on save

    def __str__(self):
        return f"{self.text} ({self.status})"
