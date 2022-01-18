from django.db import models
from django.utils import timezone
from users.models import User


class Task(models.Model):
    title = models.CharField(verbose_name='Title', max_length=240)
    user = models.ForeignKey(
        'users.User', 
        on_delete=models.CASCADE,
        verbose_name='User',
        related_name='user'
    )
    date = models.DateField(verbose_name='Date', default=timezone.now())
    done = models.BooleanField(verbose_name='Done', default=False)

    #datetime.date.today()

    def __str__(self):
        return self.title