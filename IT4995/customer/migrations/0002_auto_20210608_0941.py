# Generated by Django 3.2 on 2021-06-08 02:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='create_date',
            field=models.DateField(default=datetime.date(2021, 6, 8)),
        ),
        migrations.AlterField(
            model_name='signup',
            name='contact',
            field=models.CharField(default='', max_length=20),
        ),
    ]