from django.db import models
class Task(models.Model):
    pick = [("Not important","Not important"),("Important","Important")]
    Name = models.CharField(max_length=60)
    Brief = models.TextField()
    Task_completed = models.BooleanField(blank = True ,default=False)
    Important = models.CharField(max_length=20 , choices = pick ,default="Not important")

    def __str__(self):
        return self.Name