from django.db import models

# Create your models here.

class UserDetails(models.Model):
    user_name = models.CharField(max_length=64)
    user_age = models.IntegerField()
    MY_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    user_gender = models.CharField(max_length=20,choices= MY_CHOICES)
    user_scoolname = models.CharField(max_length=1024
    ) 
