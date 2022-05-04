from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    complete_before = models.DateField()
    creation_date = models.DateField(auto_now_add=True)
