from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    student_id = models.CharField(max_length=10, default='')
    major = models.CharField(max_length=20, default='')