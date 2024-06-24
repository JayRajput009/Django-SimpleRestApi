from django.db import models

# Create your models here.

class Userdetails(models.Models):
    user_name = models.CharField(max_length=64)
    user_age = models.IntegerField()
    MY_CHOICES = (
        ('a', 'Male'),
        ('b', 'Female'),
        ('c', 'Other'),
    )
    user_gender = models.CharField(max_length=20,choice= MY_CHOICES,default='a' )
    user_scoolname = models.CharField(max_length=1024
    ) 
