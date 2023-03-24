from django.db import models

# Create your models here.
# class Students(models.Model):
#     Name = models.CharField(max_length=25)
#     Date_of_Birth = models.DateField(max_length=15)
#     Mark = models.CharField(max_length=5)

class ToDo(models.Model):
    event = models.CharField(max_length=25)
    date = models.DateField()