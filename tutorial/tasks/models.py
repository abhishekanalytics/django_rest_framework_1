from django.db import models
from custom_user.models import CustomUser


class Task(models.Model):
    id= models.AutoField(primary_key=True)
    title =models.CharField(max_length=100,blank=True)
    description=models.CharField(max_length=1000)
    CustomUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks')