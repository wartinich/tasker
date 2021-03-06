# Generated by Django 4.0 on 2022-01-18 11:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240, verbose_name='Title')),
                ('date', models.DateField(default=datetime.datetime(2022, 1, 18, 11, 51, 30, 253952, tzinfo=utc), verbose_name='Date')),
                ('done', models.BooleanField(default=False, verbose_name='Done')),
            ],
        ),
    ]
