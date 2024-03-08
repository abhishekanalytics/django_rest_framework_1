from django.db import models


class Task(models.Model):
    id= models.AutoField(primary_key=True)
    title =models.CharField(max_length=100,blank=True)
    description=models.CharField(max_length=1000)