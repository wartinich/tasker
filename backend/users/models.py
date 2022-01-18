from django.db import models
from django.contrib.auth.models import AbstractUser 


class User(AbstarctUser):
    user_photo = models.ImageField(verbose_name='User photo', upload_to='users/', null=True, blank=True)
    date_of_birth = models.DateField(verbose_name='Birth date', null=True, blank=True)