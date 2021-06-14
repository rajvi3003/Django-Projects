from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=1000)
    date = models.CharField(max_length=50)
    status = models.BooleanField()

    def __str__(self):
        return self.task
