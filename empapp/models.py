from distutils.command.upload import upload
from django.db import models
from django.db.models import Model

class Employee(models.Model):
    name = models.CharField(max_length=50)
    emp_id = models.IntegerField()
    salary = models.FloatField()
    image = models.ImageField(upload_to='images/')
    resume = models.FileField(upload_to='resume/')

    def __str__(self):
        return self.name
