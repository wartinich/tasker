from django.db import models
from users.models import User
import datetime


class Task(models.Model):
    title = models.CharField(verbose_name='Title', max_length=240)
    user = models.ForeignKey(
        'users.User', 
        on_delete=models.CASCADE,
        verbose_name='User',
        related_name='user'
    )
    date_of_done = models.DateField(verbose_name='Date', default=datetime.datetime.today())
    done = models.BooleanField(verbose_name='Done', default=False)

    def __str__(self):
        return self.title