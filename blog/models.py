from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=64)
    mail = models.CharField(max_length=64)
    age = models.CharField(max_length=64)