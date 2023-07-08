from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=45)
    body = models.TextChoices(blank = True)
    body = models.TextField(blank=True)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title